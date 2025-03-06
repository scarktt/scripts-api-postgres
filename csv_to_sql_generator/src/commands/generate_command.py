import os

import click
import pandas as pd
from src.import_settings import database_mappings
from src.utils import save_to_file


def create_generator_commands(sql_generator_usecase):
    @click.command()
    def generate_sql_data():
        """
        Command to generate SQL data from CSV files and save them to a .sql file.
        """
        for mapping in database_mappings:
            db_name = mapping["database_name"]
            csv_path = mapping["input_files_path"]
            output_file = os.path.join(mapping["output_files_path"], f"{db_name}.sql")

            click.secho(f"\nProcessing data for database {db_name}", fg="cyan", bold=True)
            sql_statements = []

            for table in mapping["tables"]:
                if table.get("skip", False):
                    click.secho(f"\nSkipping table {table["table_name"]}", fg="cyan", bold=True)
                    continue

                file_path = os.path.join(csv_path, table["data_files"][0])

                if not os.path.exists(file_path):
                    click.secho(f"File not found: {file_path}", fg="red")
                    continue

                df = pd.read_csv(
                    file_path,
                    names=table["columns"],
                    skiprows=1 if table["ignore_first_row"] else 0,
                )

                for col in df.columns:
                    if "id" in col.lower():
                        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

                table_statements = sql_generator_usecase.generate_insert_sql(
                    table["table_name"],
                    table["columns"],
                    df,
                )

                sql_statements.extend(table_statements)
                click.secho(
                    f"Generated {len(table_statements)} SQL statements for {table['table_name']}",
                    fg="green",
                )

            output_path = mapping["output_files_path"]
            output_file = "inserts.sql"
            save_to_file(output_path, output_file, sql_statements)

    return [generate_sql_data]
