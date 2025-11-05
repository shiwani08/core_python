from books import Books

def main():
    # create a Books object (which initializes all parent classes)
    book = Books(
        user_id=1,
        username="Arijit",
        member_type="Gold Member",
        librarian_id=101,
        librarian_name="Singh",
        library_id=55,
        library_name="International Library",
        book_name="Atomic Habits",
        book_author="James Clear"
    )

    # call methods to display everything
    book.display_user()
    book.display_librarian()
    book.display_library()
    book.display_book_details()

if __name__ == "__main__":
    main()
