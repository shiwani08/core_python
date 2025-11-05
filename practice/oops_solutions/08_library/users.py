class User:
    def __init__(self, user_id, username, member_type):
        self.user_id = user_id
        self.username = username
        self.member_type = member_type
        
    def display_user(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.username}")
        print(f"Member Type: {self.member_type}")
