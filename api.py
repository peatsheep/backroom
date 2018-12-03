from flask import Flask, jsonify
from flask_cors import CORS
import service

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
  return "Hello, world!"

@app.route("/weapons")
def get_weapons():
  return jsonify(service.get_weapons())

@app.route("/armor")
def get_armor():
  return jsonify(service.get_armor())