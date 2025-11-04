from emailNotification import EmailNotification
from smsNotification import SMSNotification
from pushNotification import PushNotification

class AllNotifications():

    def __init__(self, notification):
        self.notification = notification

    def print_all_notifications(self):
        for noti in self.notification:
            print(f"{noti.__class__.__name__} Notification from the All Notifications ")

email = EmailNotification();
sms = SMSNotification();
push = PushNotification();

allNoti = AllNotifications([email, sms, push]);
allNoti.print_all_notifications()
