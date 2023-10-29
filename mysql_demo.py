# Create a database
def create_database(database_name):
    cursor = conn.cursor()
    query = f"CREATE DATABASE {database_name}"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    print(f"Database '{database_name}' created.")

# Delete the database
def delete_database(database_name):
    cursor = conn.cursor()
    query = f"DROP DATABASE {database_name}"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    print(f"Database '{database_name}' deleted.")

# Select the database
def select_database(database_name):
    conn.database = database_name
    print(f"Selected database '{database_name}'.")

# Insert records in a table
def insert_values(table, records, columns=None):
    cursor = conn.cursor()

    if columns:
        # Insert data into specified columns
        column_names = ', '.join(columns)
        placeholders = ', '.join(['%s' for _ in columns])
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
    else:
        # Insert data into all columns
        column_names = ', '.join(records.keys())
        placeholders = ', '.join(['%s' for _ in records])
        query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"

    cursor.execute(query, tuple(records.values()))

    conn.commit()
    print('Inserted records into specified columns' if columns else 'Inserted records into all columns')
    cursor.close()


# Update records in a table
def update_records(table, update_data, condition):
    cursor = conn.cursor()

    # Construct the SET clause dynamically based on update_data dictionary
    set_clause = ', '.join([f"{column} = %s" for column in update_data.keys()])
    values = list(update_data.values())

    # Construct the WHERE clause based on the condition dictionary
    where_clause = ' AND '.join(
        [f"{column} = %s" for column in condition.keys()])
    values.extend(condition.values())

    query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

    cursor.execute(query, values)

    conn.commit()
    print('Updated records')
    cursor.close()

# Delete records in a table
def delete_records(table, condition=None, delete_all=False):
    cursor = conn.cursor()

    if delete_all:
        # Delete all records in the table
        query = f"DELETE FROM {table}"
    elif condition:
        # Delete records based on a specified condition
        where_clause = ' AND '.join(
            [f"{column} = %s" for column in condition.keys()])
        values = list(condition.values())
        query = f"DELETE FROM {table} WHERE {where_clause}"
    else:
        print(
            'No delete operation specified. Use either delete_all or provide a condition.')
        return

    cursor.execute(query, values if condition else None)
    conn.commit()
    print('Deleted records')
    cursor.close()

# Select function
def select(table, columns='*', conditions=None, order_by=None, group_by=None, limit=None, offset=None):
    cursor = conn.cursor()

    query = f"SELECT {columns} FROM {table}"

    if conditions:
        query += f" WHERE {' AND '.join(conditions)}"

    if group_by:
        query += f" GROUP BY {group_by}"

    if order_by:
        query += f" ORDER BY {order_by}"

    if limit:
        query += f" LIMIT {limit}"

    if offset:
        query += f" OFFSET {offset}"

    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

# Truncate a table
def truncate_table(table_name):
    cursor = conn.cursor()
    query = f"TRUNCATE TABLE {table_name}"
    cursor.execute(query)
    conn.commit()
    cursor.close()

# Drop a table
def drop_table(table_name):
    cursor = conn.cursor()
    query = f"DROP TABLE {table_name}"
    cursor.execute(query)
    conn.commit()
    cursor.close()