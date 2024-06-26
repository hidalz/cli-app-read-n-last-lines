"""Module containing the logic to read the last N lines of a file.

:authors: Moisés Hidalgo
:since: 2024-06-26
"""

import logging
import sys

from app.exceptions import InvalidInputException


class FileReader:
    """Class encapsulating the logic to read the last N lines of a file."""

    _logger = None

    # Avoid duplicating the logs in the instances of the class (multiple CLI calls, for example)
    @classmethod
    def _setup_logging(cls) -> None:
        """Set up the logger for the class.

        It will output logs to both the console (user output) and a file (future reference).

        Args:
            cls (type): The class itself.
        """
        if cls._logger is None:
            cls._logger = logging.getLogger(f"{__name__}.{cls.__name__}")
            cls._logger.setLevel(logging.INFO)

            # Create handlers for the logger
            file_handler = logging.FileHandler("logs/app.log")
            stream_handler = logging.StreamHandler(sys.stdout)

            # Create a formatter and set it for both handlers
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)

            # Add handlers to the logger
            cls._logger.addHandler(file_handler)
            cls._logger.addHandler(stream_handler)

    def __init__(self) -> None:
        # Logging
        self.__class__._setup_logging()
        self._logger = self.__class__._logger  # Convenience, Readability, Extensibility

        # Centralized file permissions and encoding for future extension
        self._encoding = "utf-8"
        self._file_permissions = {"read": "r", "write": "w", "append": "a"}

    def _sanitize_user_input(self, file_length: int, number_of_lines: int) -> None:
        """Sanitize the user input.

        Args:
            number_of_lines (int): Number of lines to read.
            file_length (int): Number of lines in the file.

        Raises:
            InvalidInputException: If the number of lines is negative or bigger than the file length.
        """
        if number_of_lines < 0:
            raise InvalidInputException(
                {
                    "message": "The number of lines cannot be negative",
                    "number": number_of_lines,
                }
            )

        if number_of_lines > file_length:
            # self._logger.error(exc_info=e)

            raise InvalidInputException(
                {
                    "message": "The number of lines cannot be bigger than the file length",
                    "number": number_of_lines,
                    "file_length": file_length,
                }
            )
        # # File errors are not explicitly handled here because they are managed by the arguments
        # passed to the decorator in Click. Handling errors at this level would be redundant. Even
        # if this module was reused by something other than the CLI, they would be handled at a
        # lower level, where the file is actually opened (open() function). Both ways, it is
        # redundant

    def read_last_n_lines(self, file: str, number_of_lines: int) -> list[str]:
        """Reads last n lines.

        Args:
            number_of_lines (int): Number of lines to read.
            file_input (str): Path to the input file.

        Returns:
            list[str]: List of the last n lines of the file

        Raises:
            InvalidInputException: If the number of lines is negative or bigger than the file length.
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file, self._file_permissions["read"], encoding=self._encoding) as file:
                # Each element is a line of the file (stripped of the newline character)
                lines_arr = [line.rstrip("\n") for line in file.readlines()]

            file_length = len(lines_arr)

            self._sanitize_user_input(file_length, number_of_lines)

            last_n_lines = lines_arr[-number_of_lines:]
            self._logger.info("The last N lines of the input file are: %s", last_n_lines)
            return last_n_lines
        except InvalidInputException as e:
            # Capture the exception raised by the sanitization to log the error (log persistance).
            # Re-raise it to not break the program flow.
            self._logger.error("The file does not exist", exc_info=e)
            raise e
