from flask import Flask, render_template, request
from process import save_file, sno
from docpilot import boost_report
import os

app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = 'pics'


@app.route('/')
def index():
    return render_template('index.html')


def save_image(file):
    app.config['UPLOAD_FOLDER'] = 'pics'
    filename = f"{sno()}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{filename}.jpg"))
    return filename


@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    email = request.form['email']
    phoneno = request.form['phno']
    dob = request.form['dob']
    message = request.form['message']
    file = request.files['image']
    filename = save_image(file)
    file_url = boost_report(name, email, phoneno, filename)
    save_file(name, email, phoneno, dob, message, filename,file_url)
    return render_template('pass.html', n=name, id=filename)

if __name__ == '__main__':
    app.run(debug=True)
