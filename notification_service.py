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


class WhatsAppNotification(NotificationChannel):
    def send(self, message: str) -> None:
        print(f"Sending WhatsApp Message: {message}")


# STEP 2
class NotificationChannelFactory:
    _channels: dict[str, NotificationChannel] = {}

    @classmethod
    def register_channel(cls, channel: str, creator: NotificationChannel) -> None:
        if cls._channels.get(channel):
            raise ValueError(f"Channel {channel} already registered")

        cls._channels[channel] = creator

    @classmethod
    def create_channel(cls, channel: str) -> NotificationChannel:
        if creator := cls._channels.get(channel):
            return creator

        raise ValueError(f"Unknown notification channel {channel}")


NotificationChannelFactory.register_channel("sms", SMSNotification())
NotificationChannelFactory.register_channel("email", EmailNotification())
NotificationChannelFactory.register_channel("whatsapp", WhatsAppNotification())


class NotificationService:
    def send_notification(self, message: str, channel: str) -> None:
        notifier = NotificationChannelFactory.create_channel(channel)
        notifier.send(message)
