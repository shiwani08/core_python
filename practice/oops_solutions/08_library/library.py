from librarian import Librarian

class Library(Librarian):
    
    def __init__(self, user_id, username, member_type, librarian_id, librarian_name,library_id, library_name):
        super().__init__(user_id, username, member_type, librarian_id, librarian_name)
        self.library_id =library_id
        self.library_name = library_name
        
    def display_library(self):
        print(f"Library id: {self.library_id}")
        print(f"Library Name: {self.library_name}")
