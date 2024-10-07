
server = 'ufinetpowerbisql.database.windows.net'
database = 'PowerBI-Desa'
username = 'pruebaApi'
password = 'Zm6dnAkgMld5XZ9aDP30'


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