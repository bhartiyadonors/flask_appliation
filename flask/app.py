import os

from flask import Flask, request

app = Flask(__name__)
@app.route('/about',methods=['GET'])
def about():
    version = os.environ.get('APP_VERSION')

    return {'kailash_sahu_new_app_version':version},200

@app.route('/secrets',methods=['GET'])
def secrets():
    creds = dict()
    creds['db_password'] = os.environ.get('DB_PASSWORD')
    creds['app_token'] = os.environ.get('APP_TOKEN')
    creds['api_key'] = open("/run/secrets/api_key","r").read()
    creds['api_key_v2'] = open("/api_key.txt","r").read()
    return creds,200

@app.route('/config',methods=['GET'])
def config():
    config = dict()
    config['config_dev'] = open("/config-dev.yaml","r").read()
    config['config-dev-v2'] = open("/config-dev-v2.yaml","r").read()

    return config, 200
@app.route('/volumes', methods=['GET','POST'])
def volumes():
    filename = '/data/test.txt'
    if request.method == 'POST':
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write('Customer record')

            return 'saved', 201
    else:
        f = open(filename,'r')
        return f.read(), 200
