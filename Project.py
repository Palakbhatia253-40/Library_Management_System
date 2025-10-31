import streamlit as st
import pandas as pd
import os

file_path = "books.txt"


# load csv file/create----------------
def load_data():
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    
    else:
        df = pd.DataFrame(columns=["Book ID","Title","Author","Status"])
        df.to_csv(file_path,index=False)
        return df
    

# save data-----
def save_data(df):
    df.to_csv(file_path,index=False)


st.title("Library Management System")

# Session Data----------------
# Session data means temporary information related to a user's session (e.g., login details, choices, cart items, recent activity).
# Unlike variables which vanish when the program ends, session data is saved to a file so it can be reused later.
if "books" not in st.session_state:
    st.session_state.books = load_data()


# sidebar------------------------
menu = st.sidebar.selectbox("Select Option",["View Books","Add Book","Issue Book"])

if menu == "View Books":
    st.header("Books List")
    st.dataframe(st.session_state.books)

elif menu == "Add Book":
    st.header("Add Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")

    if st.button("Add"):
        if title and author:
            new_id = len(st.session_state.books)+1
            new_book = pd.DataFrame({
                "Book ID":[new_id],
                "Title":[title],
                "Author":[author],
                "Status":["Available"]
            })
            st.session_state.books=pd.concat([st.session_state.books,new_book],
                                             ignore_index=True)
            save_data(st.session_state.books)
            st.text("Book Added Sucessfully!!!!📔")

        else:
            print("Enter Both Entry!")

# Issue------------------------------
elif menu == "Issue Book":
    st.header("Issue Book")
    available = st.session_state.books[st.session_state.books["Status"]=="Available"]

    if available.empty:
        st.text("No Book Available to Issue.")

    else:
        book_id = st.selectbox("Select Book ID",available["Book ID"])
        if st.button("Issue"):
            st.session_state.books.loc[st.session_state.books["Book ID"] == book_id,"Status"]="Issued"
            save_data(st.session_state.books)
            st.text("Book Issued Successfully!!!!!📔") 



# Return-----------------------------------
elif menu=="Return Book":
    st.header("Return Book")
    issued = st.session_state.books[st.session_state.books["Status"]=="Issued"]

    if issued.empty:
        st.text("No Issued Book To Return")
    else:
        book_id=st.selectbox["Select Book ID",issued]
        if st.button("Return"):
            st.session_state.books.loc[st.session_state.books["Book ID"]==book_id,"Status"]=="Available"
            save_data(st.session_state.books)
            st.text("Book Return SucessFully!!!!!📔")