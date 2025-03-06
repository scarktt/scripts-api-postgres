from src.frameworks.database import get_database_connection
from src.repositories.console_notification_repository import ConsoleNotificationRepository
from src.repositories.sql_report_repository import SQLReportRepository
from src.usecases.report_usecase import ReportUsecase


def script():
    database = "postgresql"
    sql_connection = get_database_connection(database)

    report_repository = SQLReportRepository(sql_connection)
    notification_repository = ConsoleNotificationRepository()

    report_usecase = ReportUsecase(report_repository, notification_repository)

    report_usecase.generate_unemployed_report()


if __name__ == "__main__":
    script()
