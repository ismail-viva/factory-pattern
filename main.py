from notification_service import NotificationService

notifier = NotificationService()
notifier.send_notification("Hello, World!", "sms")
notifier.send_notification("Hello, World!", "email")
notifier.send_notification("Hello, Vivasoft!", "whatsapp")
