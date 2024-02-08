from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail
import os

# Import custom modules here:
from utils.javascript import create_metadata, render_taxonium
from utils.email import send_message

# Define and register mail handlers:
app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '8116da10dbe882'
app.config['MAIL_PASSWORD'] = '9accd47343b84e'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.secret_key = 'BLAH'
mail = Mail(app)


# Handles homepage
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

# Handles "About Us" webpage:
@app.route('/about_us', methods = ['GET'])
def about_us():
    return render_template('about_us.html')

# Handles "Contact Us" webpage:
@app.route('/contact_us', methods = ['GET', 'POST'])
def contact_us():
    if request.method == 'GET':
        return render_template('email.html')
    elif request.method == 'POST':
        name, email, institution = request.form['name'], request.form['email'], request.form['institution']
        country, message = request.form['country'], request.form['message']
        error = send_message(mail, name, email, institution, country, message)
        if error:
            return(render_template('email.html', error = error))
        flash('Message sent!')
        return(redirect(url_for('contact_us')))
        
        
# Handles page for selecting things to view:
@app.route('/selection/<gen>', methods = ['GET'])
def select(gen):
    '''
    Given a genus or a clade, display different parts of it to view (i.e., 
    Taxonium sometimes cries uncle if the newick file is too big).
    '''
    data_files = [i.split('.')[0] for i in os.listdir(f'./data/{gen}')]
    return(render_template('selection.html', head = gen.title(), choices = list(map(lambda x : x.replace('_', ' '), data_files))))

# Handles page for viewing trees:
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

# Ditto, but for the third route:
@app.route('/view_specific/<genus>/<specific>', methods = ['GET'])
def view_specific(genus, specific):
    '''
    Determines which specific element of a phylum or a things that .
    '''
    file_name, annotation_name = f'data/{genus}/{specific}.nw', f'data/annotations/{specific.replace(" ", "_")}_annotations.csv'
    raw_data, annotation_data = open(file_name).readline(), open(annotation_name).readlines()
    return render_template('view.html', meta = create_metadata(raw_data, file_name, annotation_data, annotation_name), render = render_taxonium())