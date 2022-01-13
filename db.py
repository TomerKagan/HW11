import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flask_proj'
}


def db_access(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    # We use it for INSERT, UPDATE, DELETE statements, returns the number of rows effected.
    if query_type == 'commit':
        connection.commit()
        return_value = True

    # We use it for SELECT statement, returns a result or FALSE.
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    # We close the connection and return the result
    connection.close()
    cursor.close()
    return return_value
