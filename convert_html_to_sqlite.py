import pandas as pd
import sqlite3

def html_to_sqlite(html_file, table_name, db_name):
    try:
        # Read the HTML file and parse the table
        tables = pd.read_html(html_file)
        if len(tables) == 0:
            print("No tables found in the HTML file.")
            return

        # Assuming the first table is the target
        df = tables[0]

        # Ensure the column names are valid for SQLite (no spaces or special characters)
        df.columns = [f"col_{i}" if not isinstance(col, str) else col.replace(" ", "_").replace("-", "_") for i, col in enumerate(df.columns)]

        # Print a preview of the table
        print(f"Found table with {len(df)} rows and {len(df.columns)} columns.")
        print("Preview:")
        print(df.head())

        # Connect to SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Define table structure dynamically
        columns_sql = ", ".join([f'"{col}" TEXT' for col in df.columns])
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});'
        cursor.execute(create_table_query)

        # Insert data into SQLite
        for _, row in df.iterrows():
            placeholders = ", ".join(["?"] * len(row))
            insert_query = f'INSERT INTO {table_name} VALUES ({placeholders})'
            cursor.execute(insert_query, tuple(row))

        conn.commit()
        print(f"Data successfully written to {db_name} in table '{table_name}'.")

        # Close connection
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

# File names and table name
html_file = "input.html"  # Input HTML file
db_name = "output.db"      # Output SQLite database file
table_name = "rawy_table"  # SQLite table name

# Convert HTML to SQLite
html_to_sqlite(html_file, table_name, db_name)
