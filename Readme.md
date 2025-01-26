# HTML Table to SQLite Database Conversion

This project demonstrates how to convert an HTML table into an SQLite database using Python. Below is a guide to understanding and running the provided scripts.

## Files in the Project

### 1. `convert_html_to_sqlite.py`
This script contains the logic to parse an HTML file containing a table and insert the extracted data into an SQLite database. It uses Python libraries such as `pandas` for reading the HTML table and `sqlite3` for database interactions.

### 2. `run.bat`
A batch file that automates the execution of the Python script. This makes it easier to run the conversion process on Windows systems with a single click.

## Prerequisites

1. Python 3.x installed on your system.
2. Required Python libraries:
    - `pandas`
    - `lxml`

   Install the libraries using pip:
   ```bash
   pip install pandas lxml
   ```

3. An HTML file containing the table you want to convert. Make sure the table has a structured format with `<table>`, `<thead>` (optional), and `<tbody>` tags.

## How to Use

1. **Place your HTML file** in the same directory as the script and name it `input.html`. You can modify the file name in the script if necessary.

2. **Run the conversion script**:
   - Double-click the `run.bat` file to execute the process.
   - Alternatively, you can run the Python script directly using:
     ```bash
     python convert_html_to_sqlite.py
     ```

3. **Check the output SQLite database**:
   - The script generates an SQLite database file named `output.db` (default name, customizable in the script).
   - Use any SQLite browser tool or the SQLite CLI to inspect the data.

## Example Workflow

### Sample `input.html`

### Script Explanation
The `convert_html_to_sqlite.py` file works as follows:
1. Reads the HTML file using `pandas.read_html` to extract tables.
2. Ensures column names are valid SQLite identifiers by replacing spaces and special characters.
3. Dynamically creates a table structure in the SQLite database based on the extracted table's columns.
4. Inserts all rows from the HTML table into the SQLite database.

### Running the Script
- After running the script, the `output.db` will be created with a table named `rawy_table` containing the data from the HTML table.

### Verifying the Output
You can verify the database content using an SQLite browser or by querying the database directly in Python:

```python
import sqlite3

connection = sqlite3.connect("output.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM rawy_table")
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
```

## Notes
- Ensure the HTML file is well-formed.
- Modify the script as needed for custom table structures or database schemas.

## Troubleshooting
- If the script doesn’t run, ensure all dependencies are installed and the Python executable is correctly added to your PATH environment variable.
- Use `--debug` mode (if implemented in the script) for verbose output to troubleshoot issues.

Feel free to contribute or modify this README for additional use cases or improvements!
