from flask import request, Flask
import json, socket
#imports the backend components we created in computeEngine.
from computeEngine import BackendCompute, isPrime
import hashlib
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is backend  ! ' + str(socket.gethostname()) + ' \n'

@app.route("/compute", methods=["POST"])
def compute():
    bc = BackendCompute()
    bc.compSeed()
    random.seed(bc.seed)

    limit = int(request.json['heads'])
    print("limit: ", limit)

    total_flips = bc.flip_until(int(limit))

    #Probably change this to return JSON

    x = dict()
    x["message"] = "Number of flips to get " + str(limit) + " heads in a row"
    x["hostname"] = socket.gethostname()
    x["total_flips"] = total_flips
    tmp = json.dumps(x)
    return tmp
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
