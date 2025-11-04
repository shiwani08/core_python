from notification import Notification

class PushNotification(Notification):

    def send(self):
        print("From the Push Notification")

push = PushNotification()
push.send()