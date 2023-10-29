# MySQL Database Functions Documentation

This repository contains a set of functions for interacting with a MySQL database. These functions are designed to make it easy to perform common database operations, such as creating, deleting, and selecting data from a database.

## Table of Contents

- [create_database(database_name)](#create_database)
- [delete_database(database_name)](#delete_database)
- [select_database(database_name)](#select_database)
- [insert_values(table, records, columns=None)](#insert_values)
- [update_records(table, update_data, condition)](#update_records)
- [delete_records(table, condition=None, delete_all=False)](#delete_records)
- [select(table, columns='*', conditions=None, order_by=None, group_by=None, limit=None, offset=None)](#select)
- [truncate_table(table_name)](#truncate_table)
- [drop_table(table_name)](#drop_table)

## Function Details

### create_database(database_name)

- Description: Creates a new MySQL database.
- Parameters:
  - database_name (str): The name of the new database.

### delete_database(database_name)

- Description: Deletes an existing MySQL database.
- Parameters:
  - database_name (str): The name of the database to delete.

### select_database(database_name)

- Description: Selects a MySQL database for use.
- Parameters:
  - database_name (str): The name of the database to select.

### insert_values(table, records, columns=None)

- Description: Inserts records into a MySQL table.
- Parameters:
  - table (str): The name of the table.
  - records (dict): A dictionary of records to insert.
  - columns (list): Optional. List of specific columns to insert data into.

### update_records(table, update_data, condition)

- Description: Updates records in a MySQL table based on specified conditions.
- Parameters:
  - table (str): The name of the table.
  - update_data (dict): A dictionary of columns and values to update.
  - condition (dict): A dictionary of columns and values to specify the conditions.

### delete_records(table, condition=None, delete_all=False)

- Description: Deletes records from a MySQL table based on specified conditions or deletes all records in the table.
- Parameters:
  - table (str): The name of the table.
  - condition (dict): Optional. A dictionary of columns and values to specify conditions for deletion.
  - delete_all (bool): Optional. If True, delete all records in the table.

### select(table, columns='*', conditions=None, order_by=None, group_by=None, limit=None, offset=None)

- Description: Performs a SELECT query on a MySQL table.
- Parameters:
  - table (str): The name of the table.
  - columns (str or list): Optional. The columns to retrieve (default is '*').
  - conditions (list): Optional. A list of conditions for the WHERE clause.
  - order_by (str): Optional. The column to sort results by.
  - group_by (str): Optional. The column to group results by.
  - limit (int): Optional. The maximum number of rows to retrieve.
  - offset (int): Optional. The number of rows to skip before starting to return rows.

### truncate_table(table_name)

- Description: Truncates a MySQL table, deleting all data but keeping the table structure.
- Parameters:
  - table_name (str): The name of the table to truncate.

### drop_table(table_name)

- Description: Drops (deletes) a MySQL table.
- Parameters:
  - table_name (str): The name of the table to drop.

## Usage

- Replace the placeholder values below with your actual database connection details.

```python
# Replace these placeholders with your actual database credentials
hostname = "your_database_host"
username = "your_database_username"
password = "your_database_password"
database_name = "your_database_name"

# Establish a database connection
conn = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database_name
)
```

## Author

- Minato3000

## Date

- 29/10/2023

For more information, please refer to the individual function documentation within the script file.
