from notification import Notification

class SMSNotification(Notification):

    def send(self):
        print("From the SMS Notification")

sms = SMSNotification()
sms.send()