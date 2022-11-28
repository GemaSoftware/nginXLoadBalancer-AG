from flask import request, Flask
from flask_cors import CORS, cross_origin
import requests
import json, socket
#imports the backend components we created in computeEngine.

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    url = "http://127.0.0.1:8080/"
    x = requests.get(url)

    return 'Successfully hit load_engine, now tryiing LB  ! ' + str(x.content) +' \n'

@app.route("/compute", methods=["POST"])
def compute():
    my_data = request.json['heads']
    tmp = dict()
    tmp["heads"] = my_data
    url = "http://localhost:8080/compute"
    x = requests.post(url, json=tmp)
    print(x.raw)
    return x.json()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
