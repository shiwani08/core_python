from users import User

class Librarian(User):
    def __init__(self, user_id, username, member_type, librarian_id, librarian_name):
        super().__init__(user_id, username, member_type)
        self.librarian_id = librarian_id
        self.librarian_name = librarian_name

    def display_librarian(self):
        print(f"Librarian ID: {self.librarian_id}")
        print(f"Librarian Name: {self.librarian_name}")
