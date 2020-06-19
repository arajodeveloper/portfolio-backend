from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
import smtplib
import os


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
gmail_user = os.environ['gmlu']
gmail_pw = os.environ['gmlp']


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    if request.method == 'POST':
        # request.form contains the data you sent
        # now send an email 
        import sys
        sent_from = gmail_user
        to = [gmail_user]
        subject = request.form.get('subject', '')
        body = '\n'.join([request.form.get('message', ''), request.form.get('name', ''), request.form.get('phone', ''), request.form.get('email', '')])
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_pw)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!', file=sys.stderr)
        return str(request.form)
    else:
        return 'it worked!'
