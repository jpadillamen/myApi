# API for Globant’s Data Engineering Coding Challenge
## Description
This project is a loca REST API developed in python that receive and process files to a new Database.
## Instalation
1. Clone the repository
```bash
git clone https://github.com/jpadillamen/myApi.git
```
2. Navigate to the project directory
```bash
cd myApi
```
3. Execute REST API from command line
```bash
python app.py
```
## Use
1. Una vez lanzada la aplicación, anotar la url que se necesita para llamar al servicio.
por ejemplo:
    ![image](https://github.com/user-attachments/assets/05f4accb-e10c-40d5-a6da-0005781824a7)
    en este ejemplo, la url es: http://127.0.0.1:5000
2. Desde postman o desde curl llamar al servicio, donde upload-csv es el metodo que hemos implementado y file sera la ubicación del fichero:
```bash
    curl --location --request POST 'http://127.0.0.1:5000/upload-csv' \
--form 'file=@"/C:/Users/jpadilla/AppData/Local/Programs/Python/Python311/Scripts/Globant/hired_employees.csv"'
```

5. Funciones en la librería `utils`, `sqlConnection`:

    5.1. `create_to_sql(df, targetTable)`: 
    Recibe el dataframe y el nombre de la tabla. Recupera los tipos de datos de las columnas a crear a partir de los tipos de datos que identifica en el dataframe. Si no existe la tabla, la crea en la base de datos, con los tipos de datos identificados. En mi caso son enteros o string.

    5.2. `insert_to_sql(df, targetTable)`:
    Inserta los datos del dataframe en la tabla especificada. Si la tabla no existe, primero la crea utilizando la función `create_to_sql`.
