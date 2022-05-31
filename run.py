import json
import psycopg2
import requests
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify

from classes import User, Pet, Chat

app = Flask(__name__)
CORS(app)


def execute_db_command(command, return_value=False):
    conn = psycopg2.connect(
        host="localhost",
        database="SPD",
        user="postgres",
        password="postgres")
    cursor = conn.cursor()
    cursor.execute(command)
    if return_value:
        records = cursor.fetchall()
        return records
    conn.commit()
    cursor.close()
    return 0


@app.route('/users/', methods=['POST'])
def register_user():
    json = request.json
    name = json['name']
    email = json['email']
    password = json['password']
    address = json['address']
    telephone = json['telephone']
    photo = json['photo']
    execute_db_command(f'INSERT INTO "user" VALUES (\'{name}\', \'{email}\', \'{password}\', \'{address}\', \'{telephone}\', \'{photo}\');')
    response = jsonify([])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/pets/', methods=['POST'])
def register_pet():
    json = request.json
    name = json['name']
    species = json['species']
    age = json['age']
    rga = json['RGA']
    desc = json['desc']
    castrated = json['castrated']
    wormed = json['wormed']
    vacinated = json['vacinated']
    photo = json['photo']
    gender = json['gender']
    value = json['value']
    guardianCNPJ = json['guardianCNPJ']
    execute_db_command(f'INSERT INTO "pet" VALUES (\'{name}\', \'{species}\', \'{age}\', \'{rga}\', \'{desc}\', \'{castrated}\', \'{wormed}\', \'{vacinated}\', \'{photo}\', \'{gender}\', {int(value)}, \'{guardianCNPJ}\');')
    response = jsonify([])
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/pets/', methods=['GET'])
def get_all_pets():
    keys_list = ['name','species','age','rga','desc','castrated','wormed','vacinated','photo','gender','value','guardianCNPJ']
    values = execute_db_command(f'SELECT * FROM "pet";', return_value=True)
    return_values = []
    for value in values:
        iter_dict = {}
        for key, val in zip(keys_list, value):
            iter_dict[key] = str(val).strip()
        return_values.append(iter_dict)
    response = jsonify(return_values)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/users/', methods=['GET'])
def get_users():
    keys_list = ['name', 'email', 'password', 'address', 'telephone', 'photo']
    values = execute_db_command(f'SELECT * FROM "user";', return_value=True)
    return_values = []
    for value in values:
        iter_dict = {}
        for key, val in zip(keys_list, value):
            iter_dict[key] = str(val).strip()
        return_values.append(iter_dict)
    response = jsonify(return_values)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/guardians/', methods=['GET'])
def get_guardians():
    keys_list = ['name', 'email', 'password', 'address', 'telephone', 'photo', 'CNPJ', 'category', 'CMVS', 'CMCA']
    values = execute_db_command(f'SELECT * FROM "guardian";', return_value=True)
    return_values = []
    for value in values:
        iter_dict = {}
        for key, val in zip(keys_list, value):
            iter_dict[key] = str(val).strip()
        return_values.append(iter_dict)
    response = jsonify(return_values)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
