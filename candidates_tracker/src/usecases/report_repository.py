from typing import List, Protocol

from src.entities.report import Report


class ReportRepository(Protocol):
    def get_unemployed_candidates_report(self) -> List[Report]:
        """
        Fetches a report of unemployed candidates grouped by location.
        Returns a list of Report entities.
        """
        ...
