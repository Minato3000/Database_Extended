# MySQL Database Functions

This repository contains a set of functions for interacting with a MySQL database, making common database operations easy.

- [**Create Database**](#create-database)
- [**Delete Database**](#delete-database)
- [**Select Database**](#select-database)
- [**Insert Values**](#insert-values)
- [**Update Records**](#update-records)
- [**Delete Records**](#delete-records)
- [**Select Data**](#select-data)
- [**Truncate Table**](#truncate-table)
- [**Drop Table**](#drop-table)

## Function Details

### Create Database

- **Function Name:** `create_database(database_name)`
- **Description:** Creates a new MySQL database.
- **Parameters:**
  - `database_name` (str): The name of the new database.

...

### Delete Database

- **Function Name:** `delete_database(database_name)`
- **Description:** Deletes an existing MySQL database.
- **Parameters:**
  - `database_name` (str): The name of the database to delete.

...

### Select Database

- **Function Name:** `select_database(database_name)`
- **Description:** Selects a MySQL database for use.
- **Parameters:**
  - `database_name` (str): The name of the database to select.

...

### Insert Values

- **Function Name:** `insert_values(table, records, columns=None)`
- **Description:** Inserts records into a MySQL table.
- **Parameters:**
  - `table` (str): The name of the table.
  - `records` (dict): A dictionary of records to insert.
  - `columns` (list): Optional. List of specific columns to insert data into.

...

### Update Records

- **Function Name:** `update_records(table, update_data, condition)`
- **Description:** Updates records in a MySQL table based on specified conditions.
- **Parameters:**
  - `table` (str): The name of the table.
  - `update_data` (dict): A dictionary of columns and values to update.
  - `condition` (dict): A dictionary of columns and values to specify the conditions.

...

### Delete Records

- **Function Name:** `delete_records(table, condition=None, delete_all=False)`
- **Description:** Deletes records from a MySQL table based on specified conditions or deletes all records in the table.
- **Parameters:**
  - `table` (str): The name of the table.
  - `condition` (dict): Optional. A dictionary of columns and values to specify conditions for deletion.
  - `delete_all` (bool): Optional. If True, delete all records in the table.

...

### Select Data

- **Function Name:** `select(table, columns='*', conditions=None, order_by=None, group_by=None, limit=None, offset=None)`
- **Description:** Performs a SELECT query on a MySQL table.
- **Parameters:**
  - `table` (str): The name of the table.
  - `columns` (str or list): Optional. The columns to retrieve (default is '*').
  - `conditions` (list): Optional. A list of conditions for the WHERE clause.
  - `order_by` (str): Optional. The column to sort results by.
  - `group_by` (str): Optional. The column to group results by.
  - `limit` (int): Optional. The maximum number of rows to retrieve.
  - `offset` (int): Optional. The number of rows to skip before starting to return rows.

...

### Truncate Table

- **Function Name:** `truncate_table(table_name)`
- **Description:** Truncates a MySQL table, deleting all data but keeping the table structure.
- **Parameters:**
  - `table_name` (str): The name of the table to truncate.

...

### Drop Table

- **Function Name:** `drop_table(table_name)`
- **Description:** Drops (deletes) a MySQL table.
- **Parameters:**
  - `table_name` (str): The name of the table to drop.

...

## Usage

Replace the placeholder values below with your actual database connection details:

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

<p>&nbsp;</p>

___

<p>&nbsp;</p>

**Author:** Minato3000

**Last Updated:** October 29, 2023


For more information, please refer to the individual function documentation within the script file.
