from flask import Flask, render_template
from form import ContactForm
from flask_ckeditor import CKEditor

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'
app.config['CKEDITOR_PKG_TYPE'] = 'full-all'

ckeditor = CKEditor(app)
################# Route ##################
@app.route('/')
def index():
    form = ContactForm()
   
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)