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
3. Before launching, access the file `utils\connectionStr.py` and fill in the database details.
```bash
server = 'server-url'
database = 'databaseName'
username = 'user'
password = 'password'
```   
3. Go back to the previous folder and execute the REST API from the command line.
```bash
python app.py
```
## Use
1. Once the application is launched, note down the URL needed to call the service.
	For example:
    ![image](https://github.com/user-attachments/assets/05f4accb-e10c-40d5-a6da-0005781824a7)
    in this example, the url is: http://127.0.0.1:5000
3. From Postman or curl, call the service where `upload-csv`. This is the method we have implemented and file will be the location of the file.:
```bash
    curl --location --request POST 'http://127.0.0.1:5000/upload-csv' \
--form 'file=@"/C:/Users/jpadilla/AppData/Local/Programs/Python/Python311/Scripts/Globant/hired_employees.csv"'
```
If using Postman, specify the URL, indicate that the method is POST, and in the Body section, under form-data, add a parameter file of type file. This allows us to select the file:
	![image](https://github.com/user-attachments/assets/2b4b7d0e-544a-4756-b46f-e5c37f20fd9e)

## Explanation
1. The process receives a file and performs validations on it:	

	Validate that it is a file, that it is a CSV, and that the name is one of the three possible files expected.
2. Once the information is validated, it stores the file in a dataframe. 
3. Assign columns to the dataframe based on the file name.
4. Call the functions for creation and insertion into tables.
5. Functions in the `utils.sqlConnection` library:
   
	5.1. `create_to_sql(df, targetTable)`: 
	Receives the dataframe and the table name. Retrieves the data types of the columns to be created based on the data types identified in the dataframe. If the table does not exist, it creates it in the database with the identified data types. In my case, they are integers or strings.

	5.2. `insert_to_sql(df, targetTable)`:
	Inserts the dataframe data into the specified table. If the table does not exist, it first creates it using the create_to_sql function. 7. The database where it wants to

## Contact
You can concact me via email: jpadillamen@gmail.com
