import flask
from flask import request, jsonify

from Adobetest import roman_numeral

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/romannumeral', methods=['GET']) #sets up the format of the URI
def api_roman_numeral():
    if 'query' in request.args: #finds value in the query
        query = int(request.args['query']) # extracts the value/data in the query and transforms into an integer
        d =   { #sets up the dictionary and the output format
        "input" : str(query),
        "output" : roman_numeral(query)  
        }
        return jsonify(d)

    else:
        return "Error integer not defined"
    return roman_numeral(query)
    

app.run(port=8080)
