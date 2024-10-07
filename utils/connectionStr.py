
server = 'server-url'
database = 'databaseName'
username = 'user'
password = 'password'


def obteinConnStr():

     # Create a connection string
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    return conn_str