# Django View Example
# from django.http import JsonResponse

# def send_notification(request):
#     service_type = request.GET.get("service")  # Get service from request
#     message = request.GET.get("message", "Default Message")

#     # Dependency Injection (DI) - choosing service dynamically
#     services = {
#         "email": EmailService(),
#         "sms": SMSService(),
#     }

#     service = services.get(service_type)
    
#     if not service:
#         return JsonResponse({"error": "Invalid service type"}, status=400)

#     notifier = NotificationService(service)
#     notifier.notify(message)

#     return JsonResponse({"success": f"Notification sent via {service_type}"})

from abc import ABC, abstractmethod

# Step 1: Create an abstraction (interface)
class INotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Step 2: Implement concrete services
class EmailService(INotificationService):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSService(INotificationService):
    def send(self, message):
        print(f"Sending SMS: {message}")

# Step 3: Inject dependency instead of creating it inside
class NotificationService:
    def __init__(self, service: INotificationService):  
        self.service = service  # Only holds a reference

    def notify(self, message):
        self.service.send(message)

# Client code
email_service = EmailService()  # Created once, can be reused
sms_service = SMSService()

notifier = NotificationService(email_service)  
notifier.notify("Hello via Email!")  # Uses existing EmailService

notifier = NotificationService(sms_service)  
notifier.notify("Hello via SMS!")  # Uses existing SMSService
