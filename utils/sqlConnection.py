
# sqlConnect.py

import pandas as pd
from sqlalchemy import create_engine
import pyodbc
from utils.connectionStr import obteinConnStr


def create_to_sql(df, targetTable):

    conn_str = obteinConnStr()
    typeConversion = {
        'int64': 'INTEGER',
        'object': 'VARCHAR(200)',
        'float64': 'INTEGER'
    }

    # Connect to SQL server
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    #Crear la tabla si no existe
    columns = ", ".join([f"{col} {typeConversion[str(df[col].dtype)]}" for col in df.columns])
    query = f"""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{targetTable}' AND xtype='U')
    CREATE TABLE PA.{targetTable} (
        {columns}
    );
    """
    
    #print(query)  # Imprimir la consulta y los valores
    cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla creada exitosamente")

def insert_to_sql(df, targetTable):
 
    conn_str = obteinConnStr()
    # Connect to SQL server
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

     # Reemplazar NaN con valores adecuados
    df = df.fillna('')

     # Insertar datos del DataFrame en la tabla SQL
    placeholders = ", ".join(["?" for _ in df.columns])

    # Con un batchsize de 1000 registros
    batch_size = 1000
    batch = []

    for index, row in df.iterrows():
        batch.append(tuple(row))
        if len(batch) == batch_size:
            query = f"""
            INSERT INTO PA.{targetTable} ({", ".join(df.columns)}) 
            VALUES ({placeholders})
            """
            #print(query)  # Imprimir la consulta y los valores
            cursor.executemany(query, batch)
            conn.commit()
            batch = []
    
    # Insertar si quedan registros restantes
    if batch:
        query = f"""
        INSERT INTO PA.{targetTable} ({", ".join(df.columns)}) 
        VALUES ({placeholders})
        """
        #print(query)  # Imprimir la consulta y los valores
        cursor.executemany(query, batch)
        conn.commit()
        
    conn.commit()
    cursor.close()
    conn.close()
    print("Datos insertados exitosamente")
