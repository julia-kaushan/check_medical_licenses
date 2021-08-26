import requests
from flask import Flask, request, send_file

from adapter.DataMosApi import DataMosApi
from excel.Excel import Excel

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
        excel = Excel(stream)
        list_ogrn = excel.read('ОГРН')
        try:
            api = DataMosApi()
            list_org = api.get_all(list_ogrn)
            stream = excel.build(list_org)
            return send_file(stream, mimetype='application/vnd.ms-excel', download_name='result.xlsx')
        except requests.exceptions.ConnectionError as err:
            print('Сервер не доступен', err)
            return 'Internal Server Error', 404


if __name__ == "__main__":
    app.run()


