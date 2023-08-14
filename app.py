from flask import Flask, render_template, request, jsonify

# Import custom modules here:
from utils.search import find_queries, find_entity_information

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/species_tree', methods = ['GET'])
def species_tree():
    return render_template('species_tree.html')

@app.route('/search', methods = ['GET'])
def search():
    return render_template('search.html')


# INTERNAL ROUTES - MEANT TO BE ACCESSED BY THE APPLICATION, NOT THE USER

@app.route('/find', methods = ['POST'])
def find():
    '''
    Do we still need this route?
    '''
    query = find_queries(request.data.decode('utf-8'))
    return jsonify(query)

@app.route('/find_entity', methods = ['POST'])
def find_entity():
    query = find_entity_information(request.data.decode('utf-8'))
    return jsonify(query)