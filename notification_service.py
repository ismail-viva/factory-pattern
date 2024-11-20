class NotificationService:
    def send_notification(self, message: str, channel: str) -> None:
        if channel == "sms":
            self._send_sms_notification(message)
        elif channel == "email":
            self._send_email_notification(message)
        else:
            raise ValueError(f"Unknown notification channel `{channel}`")

    def _send_sms_notification(self, message: str) -> None:
        print(f"Sending SMS: {message}")

    def _send_email_notification(self, message: str) -> None:
        print(f"Sending Email: {message}")
