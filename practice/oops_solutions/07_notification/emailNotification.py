from notification import Notification

class EmailNotification(Notification):

    def send(self):
        print("From the Email Notification")

email = EmailNotification()
email.send()