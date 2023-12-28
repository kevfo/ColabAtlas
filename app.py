from flask import Flask, render_template
import os

# Import custom modules here:
from utils.javascript import create_metadata, render_taxonium

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/selection/<gen>', methods = ['GET'])
def select(gen):
    '''
    Given a genus or a clade, display different parts of it to view (i.e., 
    Taxonium sometimes cries uncle if the newick file is too big).
    '''
    data_files = [i.split('.')[0] for i in os.listdir(f'./data/{gen}')]
    return(render_template('selection.html', head = gen.title(), choices = list(map(lambda x : x.replace('_', ' '), data_files))))

@app.route('/view/<genus>', methods = ['GET'])
def view(genus, specific = None):
    '''
    Determines which newick file the application should display.
    '''
    file_name, annotation_name = 'data/', 'data/annotations/'
    if genus.lower() == 'g':
        file_name += 'G_taxon_fulllist.nw' ; annotation_name += 'G_taxon_fulllist_annotations.csv'
    elif genus.lower() == 'r':
        file_name += 'R_taxonfull.nw' ; annotation_name += 'R_taxonfull_annotations.csv'
    raw_data, annotation_data = open(file_name).readline(), ''.join(open(annotation_name).readlines())
    return render_template('view.html', meta = create_metadata(raw_data, file_name, annotation_data, annotation_name), render = render_taxonium())

@app.route('/view_specific/<genus>/<specific>', methods = ['GET'])
def view_specific(genus, specific):
    '''
    Determines which specific element of a phylum or a things that .
    '''
    file_name, annotation_name = f'data/{genus}/{specific}.nw', f'data/annotations/{specific.replace(" ", "_")}_annotations.csv'
    raw_data, annotation_data = open(file_name).readline(), open(annotation_name).readlines()
    return render_template('view.html', meta = create_metadata(raw_data, file_name, annotation_data, annotation_name), render = render_taxonium())