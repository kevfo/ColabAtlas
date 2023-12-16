from flask import Flask, render_template

# Import custom modules here:
from utils.javascript import create_metadata, render_taxonium

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/view/<genus>', methods = ['GET'])
def view(genus):
    '''
    Change this handler later:
    '''
    raw_data, file_name = None, 'data/'
    if genus.lower() == 'g':
        file_name += 'G_taxon_fulllist.nw' 
    elif genus.lower() == 'r':
        file_name += 'R_taxonfull.nw'
    elif genus.lower() == 'v':
        file_name += 'V_taxonfull.nw'
    raw_data = open(file_name).readline()
    return render_template('view.html', meta = create_metadata(raw_data, file_name), render = render_taxonium())