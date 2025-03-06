import pandas as pd
import pytest
from src.usecases.sql_generator_usecase import SQLGeneratorUsecase


@pytest.fixture
def sql_generator():
    return SQLGeneratorUsecase()


class TestCleanTabularData:
    def test_cleaner_should_something(self, sql_generator):
        dataframe_stub = pd.DataFrame(
            {
                "id": ["14922"],
                "ocupation": ["Senior GeneXus Developer"],
                "dateRange": ["June 2014 – Present(6 years)"],
                "skills": ["{}"],
                "current_job": ["TRUE"],
                "occupation_title": ["Full Stack Engineer"],
                "start_date": ["2014-06-01 0:00:00"],
                "end_date": [""],
                "candidate_id": ["3642"],
            }
        )

        table_name = "jobs"
        table_columns = [
            "id",
            "ocupation",
            "dateRange",
            "skills",
            "current_job",
            "occupation_title",
            "start_date",
            "end_date",
            "candidate_id",
        ]
        sql_insert = sql_generator.generate_insert_sql(table_name, table_columns, dataframe_stub)

        expected_query = [
            "INSERT INTO jobs (id, ocupation, dateRange, skills, current_job, occupation_title, start_date, end_date, candidate_id) VALUES (14922, 'Senior GeneXus Developer', 'June 2014 – Present(6 years)', '{}', True, 'Full Stack Engineer', '2014-06-01 0:00:00', '', 3642);"
        ]

        assert sql_insert == expected_query
