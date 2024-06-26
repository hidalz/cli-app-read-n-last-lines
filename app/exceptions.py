"""Module containing the exceptions for the file reader.

:authors: Moisés Hidalgo
:since: 2024-06-26
"""


class FileReaderException(Exception):
    "Base class for all exceptions in this module."


class InvalidInputException(FileReaderException):
    "Exception raised when opening a file."
