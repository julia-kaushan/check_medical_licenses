import requests
import uuid
from flask import Flask, request, send_file, jsonify
from validate_email import validate_email
from FlaskApp.utils import chek_apikey
from adapter.DataMosApi import DataMosApi
from excel.Excel import Excel
from accounts.account import Account
from accounts.SqlConnection import SqlConnetion
from accounts.AccountRepository import AccountRepository

app = Flask(__name__)

ALLOWED_EXTENSIOINS = set(['xls', 'xlsx'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIOINS

@app.errorhandler(400)
def handle_bad_request(error):
    return 'bad request!', 400


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if len(request.files) == 0:
            return 'File not found', 400
        file = request.files['file']
        stream = file.stream.read()
        print(stream)
        excel = Excel(stream)
        list_ogrn = excel.read('ОГРН')
        if len(list_ogrn) == 0:
            return 'The file contains no information', 400
        print(list_ogrn)
        try:
            api = DataMosApi()
            list_org = api.get_all(list_ogrn)
            stream = excel.build(list_org)
            return send_file(stream, mimetype='application/vnd.ms-excel', download_name='result.xlsx')
        except requests.exceptions.ConnectionError as err:
            print('Сервер не доступен', err)
            return 'Internal Server Error', 404


@app.route('/info')
def get_info_org():
    ogrn = request.args.get('ogrn')
    info = DataMosApi()
    info_org = info.get(ogrn)
    return jsonify(info_org.__dict__)


@app.route('/info_list', methods=['POST'])
@chek_apikey
def get_info_list_org():
    list_ogrn = request.get_json()['ogrns']
    if len(list_ogrn) == 0:
        return 'bad request!', 400
    api = DataMosApi()
    list_org = api.get_all(list_ogrn)
    res = list(map(lambda org: org.__dict__, list_org))
    return jsonify(res)

@app.route('/register', methods=['POST'])
def register():
    email = request.get_json()['email']
    if validate_email(email) == True:
        accountRep = AccountRepository()
        account = accountRep.register(email)
        print(email)
        return jsonify(account.__dict__)
    else:
        return 'email is not correct', 401



if __name__ == "__main__":
    app.run()


