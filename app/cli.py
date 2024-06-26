"""Module containing the CLI interface for the file reader and the entry point for the program.

:authors: Moisés Hidalgo
:since: 2024-06-26
"""

import click

from app.file_reader import FileReader


class CliWrapper(FileReader):
    """Class encapsulating the logic to read the last N lines of a file using a CLI interface."""

    @classmethod
    def _setup_logging(cls) -> None:
        """Override the parent method to add the full route to the logger's name for better debugging."""
        super()._setup_logging()

        # Add full route to the logger's name for better debugging
        cls._logger.name = f"{__name__}.{cls.__base__.__name__}.{cls.__name__}"

    @staticmethod  # Avoid issues with self in the context of Click commands.
    @click.command()
    @click.version_option("0.1.0", prog_name="read_last_n_lines")
    @click.argument("file", required=True, type=click.Path(exists=True, readable=True))
    @click.argument("number_of_lines", type=int, required=True)
    def read_last_n_lines_cmd(file: str, number_of_lines: int):
        """Read the last N lines of a file."""
        # This way because we can't use cls with Click decorators
        cli_wrapper = CliWrapper()
        cli_wrapper.read_last_n_lines(file, number_of_lines)

        # CLI related error handling is done by Click itself, including negative numbers or
        # non-existent files.


if __name__ == "__main__":
    # Start the CLI program
    CliWrapper.read_last_n_lines_cmd()  # pylint: disable=no-value-for-parameter
