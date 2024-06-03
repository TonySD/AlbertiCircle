from flask import Flask, request, jsonify, render_template
from algorithms.alberti import alberti
from algorithms.alberti.mode_classes import *
from waitress import serve
from config import *

app = Flask(__name__, static_folder="static/")
MODES = [AlbertiCircleMode1, AlbertiCircleMode2, AlbertiCircleMode3, AlbertiCircleMode4, AlbertiCircleMode5]

def error(message: str):
    return jsonify({"status": 400, "error": message})

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/mode/', methods=['POST'])
def process_data():
    result = None
    data = request.get_json()
    logging.debug(f"Got json: {data}")

    if int(data['mode']) - 1 >= len(MODES):
        return error("Not valid mode")
    
    current_mode = MODES[int(data['mode']) - 1]

    if data['encrypt_mode'] == '0':
        result = current_mode.encrypt(data)
    elif data['encrypt_mode'] == '1':
        result = current_mode.decrypt(data)
    else:
        return error("Not valid encrypt_mode")
    
    logging.debug(f"Processed response: {result}")
    return jsonify(result)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    