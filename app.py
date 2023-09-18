from flask import Flask, render_template, request, jsonify

# Import custom modules here:
from utils.javascript import render_taxonium
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/species_tree', methods = ['GET'])
def species_tree():
    return render_template('species_tree.html')

@app.route('/view/<genus>', methods = ['GET'])
def view(genus):
    raw_data, file_name = None, 'data/'
    if genus == 'r':
        file_name += 'test.jsonl'
    elif genus == 'g':
        file_name += 'test.jsonl'
    elif genus == 'v':
        file_name += 'test.jsonl'
    with open(file_name) as data:
        raw_data = '\n'.join(data.readlines())
    print(raw_data)
    return render_template('view.html', js_code = render_taxonium(genus, raw_data))


'''
@app.route('/search', methods = ['GET'])
def search():
    return render_template('search.html')

@app.route('/entity/<ent>', methods = ['GET'])
def entity(ent):
    \'''
    Given an 'ent', fetch information about it and display it on a 
    separate page. 
    \'''
    entity_info = find_entity_information(ent)
    return render_template('entity_page.html', info = entity_info)

# INTERNAL ROUTES - MEANT TO BE ACCESSED BY THE APPLICATION, NOT THE USER

@app.route('/find', methods = ['POST'])
def find():
    \'''
    Do we still need this route (i.e., for that search bar page)?
    \'''
    query = find_queries(request.data.decode('utf-8'))
    return jsonify(query)

@app.route('/find_information/<item>', methods = ['POST'])
def find_information(item):
    \'''
    Returns number of missing entities and also text color.
    \'''
    req = item.lower()
    return jsonify({'text_color' : get_color(req), 
                    'missing' : find_entity_information(req),
                    'is_species' : is_species(req)})
    
@app.route('/populate_item/<item>', methods = ['GET', 'POST'])
def populate_item(item):
    \'''
    Given an item, try to find its nested species.
    \'''
    req = item.split('(')[0].strip().lower()
    return jsonify({'species' : find_species(req)})





# Not sure if still need these routes...

@app.route('/find_entity', methods = ['POST'])
def find_entity():
    query = find_entity_information(request.data.decode('utf-8'))
    return jsonify(query)

@app.route('/find_color/', methods = ['POST'])
def find_color():
    query = ''.join([i for i in request.data.decode('utf-8').split()[-1] if not i.isdigit()]).lower()
    print(query, get_color(query))
    return jsonify(get_color(query))
'''