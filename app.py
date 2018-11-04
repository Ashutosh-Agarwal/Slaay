import os

from flask import Flask, request
from werkzeug.utils import secure_filename

from predict import prediction
from charge_credit_card import *
from credential import * 

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
p_dict = {0: 'FASTRACK 3072SAA322', 1: 'MVMT Classic', 2: 'TIMEX T2N943'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return '<html><body><p>Wrong Image sent</p></body></html>'
        file = request.files['file']

        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return '<html><body><p>Empty Image sent</p></body></html>'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            index = prediction(UPLOAD_FOLDER + filename).flatten().argmax()
            return p_dict[index]
    return "<html><body><p>Connection Error 404</p></body></html>"

@app.route('/payment', methods=['POST'])
def charge():
    transaction = payment(name,key,"4111111111111111", "2020-12", '10.55', "MerchantID-0001")
    return transaction

if __name__ == '__main__':
    app.secret_key = 'SomeRandomString'
    app.run(host='0.0.0.0', port=8080)

