# YCSV

YCSV - CSV in a terminal with a graphic using the curses library.

![YCSV](image/YCSVα1.png)

## Features

- Displays CSV data in a terminal window with a graphical representation.
- Supports navigation through CSV data rows and columns.
- Provides customizable column widths for better readability.
- Shows file metadata including the last modified date.

## Prerequisites

- Python 3
- Pandas
  ```bash
    pip install pandas
  ```
- Curses

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/marshmeowllo/YCSV.git
    cd ycsv
    ```

2. Run the application by providing a CSV file path as a command-line argument:

    ```bash
    python ycsv.py /path/to/your/csv/file.csv
    ```

3. Use arrow keys or other navigational keys to explore the CSV data.

4. Press any key to quit and exit the application.
