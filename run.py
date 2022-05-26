import psycopg2
from flask import Flask, request, render_template

from classes import User, Pet, Chat

app = Flask(__name__)


def execute_db_command(command):
    conn = psycopg2.connect(
        host="localhost",
        database="SPD",
        user="postgres",
        password="postgres")
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()
    cursor.close()


@app.route('/register_user', methods=['POST'])
def register_user():
    json = request.json
    name = json['name']
    email = json['email']
    password = json['password']
    address = json['address']
    telephone = json['telephone']
    photo = json['photo']
    execute_db_command(f'INSERT INTO "user" VALUES (\'{name}\', \'{email}\', \'{password}\', \'{address}\', \'{telephone}\', \'{photo}\');')
    return 'user registered'


@app.route('/register_pet', methods=['POST'])
def register_pet():
    json = request.json
    name = json['name']
    species = json['species']
    age = json['age']
    rga = json['rga']
    desc = json['desc']
    castrated = json['castrated']
    wormed = json['wormed']
    vacinated = json['vacinated']
    photo = json['photo']
    gender = json['gender']
    value = json['value']
    guardianCNPJ = json['guardianCNPJ']
    execute_db_command(f'INSERT INTO "pet" VALUES (\'{name}\', \'{species}\', \'{age}\', \'{rga}\', \'{desc}\', \'{castrated}\', \'{wormed}\', \'{vacinated}\', \'{photo}\', \'{gender}\', {int(value)}, \'{guardianCNPJ}\');')
    return 'pet registered'


@app.route('/get', methods=['get'])
def get_pet():
    json = request.json
    name = json['name']
    species = json['species']
    age = json['age']
    rga = json['rga']
    desc = json['desc']
    castrated = json['castrated']
    wormed = json['wormed']
    vacinated = json['vacinated']
    photo = json['photo']
    gender = json['gender']
    value = json['value']
    guardianCNPJ = json['guardianCNPJ']
    execute_db_command(f'INSERT INTO "pet" VALUES (\'{name}\', \'{species}\', \'{age}\', \'{rga}\', \'{desc}\', \'{castrated}\', \'{wormed}\', \'{vacinated}\', \'{photo}\', \'{gender}\', {int(value)}, \'{guardianCNPJ}\');')
    return 'pet registered'



@app.route('/login', methods=['POST'])
def login():
    json = request.json
    email = json['email']
    password = json['password']
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
