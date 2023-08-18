from flask import Flask, render_template, request, jsonify

# Import custom modules here:
from utils.search import find_queries, find_entity_information, get_color

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
    Do we still need this route (i.e., for that search bar page)?
    '''
    query = find_queries(request.data.decode('utf-8'))
    return jsonify(query)

@app.route('/find_entity', methods = ['POST'])
def find_entity():
    query = find_entity_information(request.data.decode('utf-8'))
    return jsonify(query)

@app.route('/find_color/', methods = ['POST'])
def find_color():
    query = ''.join([i for i in request.data.decode('utf-8').split()[-1] if not i.isdigit()]).lower()
    print(query, get_color(query))
    return jsonify(get_color(query))