import re

import pandas as pd


class DataCleanerUseCase:
    def clean_tabular_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the given DataFrame by applying _clean_text to every cell.
        (Uses applymap for element-wise processing.)
        """
        return df.applymap(self._clean_text)

    def _clean_text(self, value):
        # Convert to string (handles NaN as well) and strip whitespace
        value = str(value).strip()

        # Remove invisible Unicode characters
        value = re.sub(r"[\u200b\u200c\u200d\u2060\ufeff]", "", value)

        # Replace multiple spaces with a single space
        value = re.sub(r"\s+", " ", value)

        # Remove all double quotes
        value = value.replace('"', "")

        # Collapse any occurrence of two or more consecutive commas into one
        while ",," in value:
            value = value.replace(",,", ",")

        return value
