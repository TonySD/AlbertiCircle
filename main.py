from flask import Flask, request, jsonify, render_template
from algorithms.alberti import alberti
from waitress import serve
from config import *

app = Flask(__name__, static_folder="static/")

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/mode/', methods=['POST'])
def process_data():
    data = request.get_json()
    result = {"ciphertext": data['ciphertext'].upper(), "key": data["key"], "password": "", "indicator": "", "plaintext": ""}
    logging.debug(f"Got json: {data}")

    if data['mode'] == '1':
        result['plaintext'] = alberti.mode1(result['ciphertext'], result['key'])
    elif data['mode'] == '2':
        result['plaintext'] = alberti.mode2(data['ciphertext'], result['key'])
    elif data['mode'] == '3':
        if data['indicator'] == "" or len(data['indicator']) > 1:
            result['plaintext'] = "<br />".join(alberti.mode3(data['ciphertext'], result['key']))
        else:
            result['indicator'] = data['indicator']
            result['plaintext'] = alberti.mode3(data['ciphertext'], result['key'], data['indicator'])
    elif data['mode'] == '4':
        result['plaintext'] = alberti.mode4(data['ciphertext'], result['key'])
    elif data['mode'] == '5':
        if data['password'] != "":
            result['password'] = data['password']
            result['plaintext'] = alberti.mode5(data['ciphertext'], result['key'], data['password'])
        else:
            result['plaintext'] = alberti.mode5(data['ciphertext'], result['key'])
    logging.debug(f"Processed response: {result}")
    return jsonify(result)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)