from typing import Callable

import click


def create_click_command(commands: list) -> Callable:
    """
    Creates a Click CLI group and register received commands.
    commands: List of functions that acts as a Click commands.
    """

    @click.group()
    def cli():
        """
        Command Line Interface for the project.
        """
        pass

    if commands:
        for command in commands:
            cli.add_command(command)

    return cli
