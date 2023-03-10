from flask import Flask, jsonify, request
from sqlalchemy import create_engine, text
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
# 1.Ruta para obtener todos los libros
@app.route('/', methods=['GET'])
def get_all_barrios():
    # Crea un motor de conexion a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:fmfDYbapmP6bshyuX3rz@containers-us-west-138.railway.app:6177/railway')
    query = text('SELECT * FROM barrios')
    df = pd.read_sql_query(query, engine.connect())
    return jsonify(df.to_json())
    
@app.route('/nombre', methods=['GET'])
def get_barrio_name():
    nombre = request.args['Nombre']
    # Crea un motor de conexion a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:fmfDYbapmP6bshyuX3rz@containers-us-west-138.railway.app:6177/railway')
    query = text(f"""SELECT * FROM "barrios" where "Nombre" ='{nombre}'""")
    df = pd.read_sql_query(query, engine.connect())
    return jsonify(df.to_json())

@app.route('/area', methods=['GET'])
def get_barrio_area():
    min = request.args['min']
    max = request.args['max']
    # Crea un motor de conexion a la base de datos PostgreSQL
    engine = create_engine('postgresql://postgres:fmfDYbapmP6bshyuX3rz@containers-us-west-138.railway.app:6177/railway')
    query = text(f"""SELECT * FROM "barrios" WHERE 
                    "Areas de barrios"  >= {min} AND "Areas de barrios" <= {max}""")
    df = pd.read_sql_query(query, engine.connect())
    return jsonify(df.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
