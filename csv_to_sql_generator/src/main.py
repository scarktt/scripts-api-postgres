from src.commands import create_clean_commands, create_generator_commands
from src.frameworks.cli import create_click_command
from src.usecases.data_cleaner_usecase import DataCleanerUseCase
from src.usecases.sql_generator_usecase import SQLGeneratorUsecase

# Usecases
data_cleaner_usecase = DataCleanerUseCase()
sql_generator_usecase = SQLGeneratorUsecase()

# CLI commands
clean_commands = create_clean_commands(data_cleaner_usecase)
generator_commands = create_generator_commands(sql_generator_usecase)


cli = create_click_command(commands=[*clean_commands, *generator_commands])

if __name__ == "__main__":
    cli()
