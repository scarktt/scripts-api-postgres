import pandas as pd
import pytest
from src.usecases.data_cleaner_usecase import DataCleanerUseCase


@pytest.fixture
def cleaner():
    return DataCleanerUseCase()


class TestCleanTabularData:
    def test_cleaner_should_remove_non_printable_characters(self, cleaner):
        dataframe_stub = pd.DataFrame(
            {
                "name": ["Some text in a column​"],
            }
        )

        dataframe_expected = pd.DataFrame(
            {
                "name": ["Some text in a column"],
            }
        )

        dataframe_cleaned = cleaner.clean_tabular_data(dataframe_stub)

        pd.testing.assert_frame_equal(
            dataframe_cleaned.reset_index(drop=True), dataframe_expected.reset_index(drop=True)
        )

    def test_cleaner_should_trim_whitespaces(self, cleaner):
        dataframe_stub = pd.DataFrame(
            {
                "name": [" Some text in a column "],
            }
        )

        dataframe_expected = pd.DataFrame(
            {
                "name": ["Some text in a column"],
            }
        )

        dataframe_cleaned = cleaner.clean_tabular_data(dataframe_stub)

        pd.testing.assert_frame_equal(
            dataframe_cleaned.reset_index(drop=True), dataframe_expected.reset_index(drop=True)
        )

    def test_cleaner_should_remove_inner_quotes(self, cleaner):
        dataframe_stub = pd.DataFrame(
            {
                "skills": [
                    "{Node.js,"
                    "AWS Lambda"
                    ","
                    "Amazon S3"
                    ","
                    "OpenAPI Specification (OAS)"
                    ",PostgreSQL,TypeScript}"
                ],
            }
        )

        expected_text = (
            "{Node.js,AWS Lambda,Amazon S3,OpenAPI Specification (OAS),PostgreSQL,TypeScript}"
        )

        dataframe_cleaned = cleaner.clean_tabular_data(dataframe_stub)
        # print("dataframe_cleaned: ", dataframe_cleaned["skills"].iloc[0])

        assert dataframe_cleaned["skills"].iloc[0] == expected_text
