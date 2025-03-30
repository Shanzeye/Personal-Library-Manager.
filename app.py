import streamlit as st
import pandas as pd

# Function to initialize the library as an empty list
def initialize_library():
    if 'library' not in st.session_state:
        st.session_state['library'] = []

# Function to add a book to the library
def add_book(title, author, genre, year):
    book = {
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Year': year
    }
    st.session_state['library'].append(book)

# Function to display the library
def display_library():
    if len(st.session_state['library']) == 0:
        st.write("No books in the library yet.")
    else:
        library_df = pd.DataFrame(st.session_state['library'])
        st.dataframe(library_df)

# Function to search the library
def search_books(query):
    query = query.lower()
    results = [book for book in st.session_state['library'] if query in book['Title'].lower() or query in book['Author'].lower() or query in book['Genre'].lower()]
    if len(results) == 0:
        st.write("No matching books found.")
    else:
        results_df = pd.DataFrame(results)
        st.dataframe(results_df)

# Function to delete a book
def delete_book(title):
    st.session_state['library'] = [book for book in st.session_state['library'] if book['Title'].lower() != title.lower()]
    st.write(f"Book titled '{title}' has been deleted.")

# Streamlit UI
st.title("📚 Library Manager")

# Initialize library
initialize_library()

# Sidebar for navigation
option = st.sidebar.selectbox("Select an action", ["Add Book", "View Library", "Search Books", "Delete Book"])

if option == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year of Publication", min_value=1000, max_value=2025, step=1)

    if st.button("Add Book"):
        if title and author and genre and year:
            add_book(title, author, genre, year)
            st.success(f"Book '{title}' added to the library.")
        else:
            st.warning("Please fill in all the fields.")

elif option == "View Library":
    st.subheader("Library Collection")
    display_library()

elif option == "Search Books":
    st.subheader("Search for a Book")
    query = st.text_input("Search by Title, Author, or Genre")
    if st.button("Search"):
        search_books(query)

elif option == "Delete Book":
    st.subheader("Delete a Book")
    title_to_delete = st.text_input("Enter the title of the book to delete")
    if st.button("Delete Book"):
        if title_to_delete:
            delete_book(title_to_delete)
        else:
            st.warning("Please enter the title of the book you want to delete.")

