class ConsoleNotificationRepository:
    def notify(self, message: str) -> None:
        print(f"sending message: {message}")
