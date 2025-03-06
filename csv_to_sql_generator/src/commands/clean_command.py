import os

import click
import pandas as pd


def create_clean_commands(data_cleaner_usecase):
    @click.command()
    @click.argument(
        "input_dir",
        type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    )
    @click.argument(
        "output_dir",
        type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True),
    )
    def clean_data(input_dir, output_dir):
        """
        Cleans CSV files from INPUT_DIR and saves the cleaned versions to OUTPUT_DIR.
        """
        click.secho(f"Cleaning CSV files from: {input_dir}", fg="yellow", bold=True)
        os.makedirs(output_dir, exist_ok=True)

        for file_name in os.listdir(input_dir):
            if file_name.endswith(".csv"):
                input_path = os.path.join(input_dir, file_name)
                output_path = os.path.join(output_dir, file_name.lower())

                try:
                    df = pd.read_csv(input_path, dtype=str)

                    df_cleaned = data_cleaner_usecase.clean_tabular_data(df)
                    df_cleaned.to_csv(output_path, index=False)

                    click.secho(f"✔ Cleaned: {file_name} → {output_path}", fg="green", bold=True)
                except Exception as e:
                    click.secho(f"❌ Error processing {file_name}: {e}", fg="red", bold=True)

        click.secho("✅ Data cleaning completed!", fg="cyan", bold=True)

    return [clean_data]
