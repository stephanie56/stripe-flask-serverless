import stripe
import os

from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/public-keys')
def public_keys():
    return jsonify({'key': os.getenv('STRIPE_PUBLISHABLE_KEY')})


app.run(port=4242)
