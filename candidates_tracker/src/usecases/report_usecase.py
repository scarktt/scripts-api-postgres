from src.usecases.notification_repository import NotificationRepository
from src.usecases.report_repository import ReportRepository


class ReportUsecase:
    def __init__(
        self,
        report_repository: ReportRepository,
        notification_repository: NotificationRepository,
    ):
        self.report_repository = report_repository
        self.notification_repository = notification_repository

    def generate_unemployed_report(self) -> None:
        reports = self.report_repository.get_unemployed_candidates_report()

        total_unemployed = sum(report.unemployed_per_location for report in reports)

        if reports:
            most_unemployed_location = reports[0].location
            most_unemployed_count = reports[0].unemployed_per_location
        else:
            most_unemployed_location = "N/A"
            most_unemployed_count = 0

        message = (
            f"Found {total_unemployed} candidates without a job. "
            f"The location with the most unemployed candidates is {most_unemployed_location} "
            f"with {most_unemployed_count} candidates."
        )

        self.notification_repository.notify(message)
