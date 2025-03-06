import pandas as pd


class SQLGeneratorUsecase:
    def generate_insert_sql(
        self,
        table_name: str,
        columns: list,
        df: pd.DataFrame,
    ) -> list:
        """
        Generates SQL INSERT statements from a DataFrame.
        Converts NaN values to NULL and ensures ID columns are not wrapped in quotes.
        """
        sql_statements = []

        for _, row in df.iterrows():
            formatted_values = []

            for col, value in zip(columns, row):
                convert = self._conversion_factory(col)
                formatted_values.append(convert(value))

            values = ", ".join(formatted_values)
            sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values});"
            sql_statements.append(sql)

        return sql_statements

    def _conversion_factory(self, column_name: str):
        """
        Factory that returns a function to convert values based on the column
        name.
        """

        def convert(value):
            if pd.isna(value):
                return "NULL"

            if isinstance(value, str) and value.upper() in ["TRUE", "FALSE"]:
                return str(bool(value))

            if "id" in column_name.lower():
                try:
                    return str(int(value))
                except (ValueError, TypeError):
                    return str(value)

            return f"'{str(value).replace("'", "''")}'"

        return convert
