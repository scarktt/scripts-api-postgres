from typing import Protocol


class NotificationRepository(Protocol):
    def notify(self, message: str) -> None:
        """
        Sends a notification with the given message.
        """
        ...
