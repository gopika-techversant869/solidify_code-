"""
Let’s consider a User Notification Service in a web application where we send notifications via Email or SMS.

"""

class EmailService:
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSService:
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, service_type):
        if service_type == "email":
            self.service = EmailService()  # Creates a new EmailService object
        elif service_type == "sms":
            self.service = SMSService()  # Creates a new SMSService object
        else:
            raise ValueError("Invalid service type")

    def notify(self, message):
        self.service.send(message)

notifier = NotificationService("email")  # Creates EmailService object
notifier.notify("Hello via Email!")

notifier = NotificationService("sms")  # Creates new SMSService object
notifier.notify("Hello via SMS!")

notifier = NotificationService("email")  # Creates another email object 
notifier.notify("Hello via Email!")