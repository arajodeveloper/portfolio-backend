from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    if request.method == 'POST':
        # request.form contains the data you sent
        # now send an email 
        return str(request.form)
    else:
        return 'LOL'
