import logging

from src.entities.report import Report


class SQLReportRepository:
    def __init__(self, sql_connection):
        self.sql_connection = sql_connection

    def get_unemployed_candidates_report(self):
        try:
            with self.sql_connection.cursor() as cursor:
                query = """
                SELECT c.location, COUNT(DISTINCT c.id) AS unemployed_per_location
                FROM candidates c
                LEFT JOIN jobs j ON c.id = j.candidate_id
                WHERE j.current_job IS NULL OR j.current_job = FALSE
                GROUP BY c.location
                ORDER BY unemployed_per_location DESC;
                """
                cursor.execute(query)
                candidates = cursor.fetchall()

                reports = [
                    Report(location=row[0], unemployed_per_location=row[1]) for row in candidates
                ]
                return reports
        except Exception as e:
            logging.error(f"Error fetching candidates: {e}")
            raise
