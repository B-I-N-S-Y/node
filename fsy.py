import flask
from flask import jsonify


app = flask.Flask(__name__)

# test data
tpe = {"response":"yes"}


cities = tpe


@app.route('/', methods=['GET'])
def cities_all2():
    return jsonify(cities)

@app.route('/api/v1.6/privileged-request',methods=['POST'])
def cities_all():
    return jsonify(cities)

#/api/v1.6/privileged-request

if __name__ == '__main__':
    app.debug = True

app.run(host='0.0.0.0',port='443',ssl_context=('server.crt', 'server.key'))
