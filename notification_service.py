# STEP  1
from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        ...


class SMSNotification(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"Sending SMS: {message}")


class EmailNotification(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"Sending Email: {message}")


# STEP 2
class NotificationChannelFactory:
    @staticmethod
    def create_channel(channel: str) -> NotificationChannel:
        if channel == "sms":
            return SMSNotification()
        elif channel == "email":
            return EmailNotification()
        else:
            raise ValueError(f"Unknown notification channel `{channel}`")

class NotificationService:
    def send_notification(self, message: str, channel: str) -> None:
        notifier = NotificationChannelFactory.create_channel(channel)
        notifier.send(message)
