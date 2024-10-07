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
3. Antes de lanzar acceder a fichero utils\connectionStr.py, y rellenar los datos de la base de datos.
```bash
server = 'server-url'
database = 'databaseName'
username = 'user'
password = 'password'
```   
3. Volver a carpeta anterior y Execute REST API from command line
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
si se utiliza postman, indicar la url, indicar que el metodo es POST, y en la sección Body, en form-data añadir un parametro file de tipo file.
Esto nos permite seleccionar el fichero:
![image](https://github.com/user-attachments/assets/2b4b7d0e-544a-4756-b46f-e5c37f20fd9e)

## Explanation
1. El proceso recibe un fichero y realiza validaciones sobre este: Que sea un fichero, que sea csv, que el nombre sea uno de los tres posibles ficheros que espera.
2. Una vez que valida la información, almacena el fichero en un dataframe.
3. Al dataframe le asigna columnas en función del nombre de fichero.
4. Llama a las funciones de creacion e inserción en tablas.
5. Funciones en la librería `utils`, `sqlConnection`:
    5.1. `create_to_sql(df, targetTable)`: 
    Recibe el dataframe y el nombre de la tabla. Recupera los tipos de datos de las columnas a crear a partir de los tipos de datos que identifica en el dataframe. Si no existe la tabla, la crea en la base de datos, con los tipos de datos identificados. En mi caso son enteros o string.
    5.2. `insert_to_sql(df, targetTable)`:
    Inserta los datos del dataframe en la tabla especificada. Si la tabla no existe, primero la crea utilizando la función `create_to_sql`.
6. La base de datos donde se quiere 
## Contact
You can concact me via email: jpadillamen@gmail.com
