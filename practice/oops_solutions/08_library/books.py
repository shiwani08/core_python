from library import Library

class Books(Library):
    
    def __init__(self, user_id, username, member_type, librarian_id, librarian_name, library_id, library_name, book_name, book_author):
        
        super().__init__(user_id, username, member_type, librarian_id, librarian_name,library_id, library_name)
        
        self.book_name = book_name
        self.book_author = book_author
    
    def display_book_details(self):
        print(f"Book name: {self.book_name}")
        print(f"Book author: {self.book_author}")
