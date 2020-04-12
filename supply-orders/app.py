from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

from flask import send_file

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

import json
from flask import jsonify, request

@app.route('/collect',  methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))

    answers = memory['twilio']['collected_data']['collect_supplies_order']['answers']

    first_name = answers['first_name']['answer']
    supply_type = answers['supply_type']['answer']
    num_supplies = answers['num_supplies']['answer']

    message = (
        f'Ok {first_name}. Your order for {num_supplies} {supply_type} is now confirmed.'
        f' Thank you for ordering with us'
    )

    return jsonify(actions=[{'say': {'speech': message}}])