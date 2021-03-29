import flask
from flask import request, jsonify
import mysql.connector

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def initialize_database_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        database="proto",
        password="dreamhope",
        auth_plugin='mysql_native_password'
    )

def query_database(database_connection, query):
    db_cursor = database_connection.cursor()
    db_cursor.execute(query)
    return db_cursor.fetchall()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sample model host</h1>
<p>basic modeling prototype</p>'''


@app.route('/api/v1/model/demographic', methods=['GET'])
def api_demographic():
    # ensure user gets handling messages
    if 'id_person' in request.args:
        id_person = request.args['id_person']
        query = "select id_person, id_demographic from person where id_person = " + id_person
    else:
        return "please check documentaton"

    demographic = query_database(
        initialize_database_connection(), 
        query)

    return jsonify(demographic)

@app.route('/api/v1/model/recommendation', methods=['GET'])
def api_recommendation():
    if 'id_person' in request.args and 'limit' in request.args:
        id_person = request.args['id_person']
        limit = request.args['limit']
    else:
        return "please check documentation"

    db = initialize_database_connection()
    query = 'select id_person, id_offer from person inner join demographic on person.id_demographic = demographic.id_demographic where rank_offer <= ' + \
        limit + ' and id_person = ' + id_person
    recommendation = query_database(db, query)
    return jsonify(recommendation)

app.run()



