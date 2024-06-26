# Last N Lines Reader

This project offers a solution to the task of reading the last N lines from a given file. Designed with a focus on reliability, it incorporates logging, exception handling, and secure operations. The simplicity of the core functionality shows the architecture behind it, aimed at demonstrating best practices in software development in Python. These focus on effective logging strategies & exception handling and secure handling of edge cases.

## Getting Started

### Prerequisites

Python 3.10+

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/hidalz/cli-app-read-n-last-lines.git
```

2. Navigate to the project directory:

```bash
cd cli-app-read-n-last-lines
```

3. Install the requirements:

```bash
export PYTHONPATH=.
pip install -r requirements.txt
```

## Usage

To use the application, run the main.py script with Python. The script is designed to be executed from the command line. Here's how you can read the last N lines from a file:

1. Open your terminal.
2. Run the following command:

```bash
python3 main.py <file_path> <number_of_lines>
```

- `file_path`: The path to the file from which to read the last N lines. This path must point to an existing and readable file.
- `number_of_lines`: The number of lines to read from the end of the file.

## Features

- **Read Last N Lines**: Employs a readable approach to read the last N lines from a file, ideal for analyzing log files or accessing recent data entries.
- **Logging**: Features a comprehensive logging system that facilitates detailed debugging and continuous monitoring of the application's performance.
- **Exception Handling**: Implements thorough exception handling mechanisms to manage and mitigate potential errors, ensuring the application's stability and security.
- **Configurable Settings**: Allows users to easily configure settings such as the number of lines to read and the specific files to analyze, providing flexibility.

## Architecture

The CLIWrapper expands the capabilities of the FileReader class to incorporate a command-line interface (CLI) for accessing the last N lines of a file. This improvement aims to provide a user-friendly method for interacting with the features of our file reading utility directly from the terminal.

- Custom Logging Setup: Overriding the _setup_logging method from its parent class, CLIWrapper introduces a more detailed logging name scheme. This includes the full route (module.classname) in the logger's name, improving debugging and log tracking by providing clearer context in log messages.

Traces are stored into the logs as well for stored traceability options.

## O(n) Complexity

The current implementation reads the last N lines of a file in a O(n) time & space complexity.

Complexity can be improved to O(m) time where m is the size of the file in bytes from the end up to the nth newline, by reading the file in reverse order and stopping when the number of lines is reached.

The space complexity can be improved to O(k), where k is the total number of characters in the last n lines. This is typically much smaller than n (the total number of lines in the file).

Such a solution would be more memory and time-efficient for large files, as it would not require reading the entire file into memory. This would also allow for reading the last n lines of very large files that do not fit into memory.

However, as a POC, the current implementation is sufficient and more readable.

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest features.

## License

This project is licensed under the MIT License. Check [LICENSE.md](LICENSE.md) for details.
