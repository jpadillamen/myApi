from flask import Flask, request, jsonify
from utils.sqlConnection import insert_to_sql,create_to_sql
from utils.connectionStr import obteinConnStr
import pandas as pd
import os

app = Flask(__name__)

@app.route('/holaMundo', methods=['GET'])
def prueba():
    return 'holaMundo 12345'

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    # Verifica si se recibe algun archivo.
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    # Verifica si el archivo tiene un nombre, 
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    fileName = file.filename

    # Verifica si el archivo es un CSV
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'File type not allowed. Only CSV files are accepted.'}), 400

    #Verificar que el nombre del fichero esta entre los tres que puede leer
    if (file.filename not in {'jobs.csv','hired_employees.csv','departments.csv' }):
        return jsonify({'error': 'Not a valid file Name'}), 400

    targetTable = fileName.replace(".csv","")

    # Lee el archivo CSV utilizando pandas
    try:
        df = pd.read_csv(file, header=None)
        if (targetTable =='jobs'):
            df.columns = ['id', 'job']
        if (targetTable =='departments'):
            df.columns = ['id', 'department']
        if (targetTable =='hired_employees'):
            df.columns = ['id', 'name','datetime','department_id','job_id']
        create_to_sql(df, targetTable)
        insert_to_sql(df, targetTable)
        # Mostrar en pantalla contenido fichero.
        #return jsonify({'message': 'CSV file received and loaded successfully', 'data': create_to_sql(df, targetTable)}), 200
        return jsonify({'message': 'CSV file received and loaded in table successfully', 'data': df.to_dict(orient='records')}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)