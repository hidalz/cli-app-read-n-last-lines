from unittest import TestCase, main

from app.exceptions import InvalidInputException
from app.file_reader import FileReader


# Docstrings for the class or methods are not necessary in this context.
class TestLastNFiles(TestCase):
    def setUp(self):
        self.file_reader = FileReader()  # DRY

    def test_last_n_files_positive(self):
        last_n_lines = self.file_reader.read_last_n_lines(
            number_of_lines=5, file="data/test_data/file.txt"
        )

        # Check if the last 5 lines are read correctly. This also asserts the length of the list
        assert last_n_lines == ["6", "7", "8", "9", "10"]

    def test_last_n_files_longer_input_than_file_length(self):
        with self.assertRaises(InvalidInputException):
            self.file_reader.read_last_n_lines(number_of_lines=11, file="data/test_data/file.txt")

    # Fallback test. Handled by Click, but good to have if the module is used elsewhere.
    def test_last_n_files_negative_input(self):
        with self.assertRaises(InvalidInputException):
            self.file_reader.read_last_n_lines(number_of_lines=-1, file="data/test_data/file.txt")

    def test_last_n_files_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            self.file_reader.read_last_n_lines(
                number_of_lines=5, file="data/test_data/non_existent_file.txt"
            )


if __name__ == "__main__":
    main()
