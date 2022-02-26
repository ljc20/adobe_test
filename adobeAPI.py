import flask
from flask import request, jsonify

from Adobetest import roman_numeral

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/romannumeral', methods=['GET'])
def api_roman_numeral():
    if 'query' in request.args:
        query = int(request.args['query'])
        d =   {
        "input" : str(query),
        "output" : roman_numeral(query)  
        }
        return jsonify(d)

    else:
        return "Error integer not defined"
    return roman_numeral(query)
    

app.run(port=8080)
