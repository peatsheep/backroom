from flask import Flask, jsonify
from flask_cors import CORS
import service

app = Flask(__name__)
CORS(app)

@app.route("/weapons")
def get_weapons():
  return jsonify(service.get_weapons())

@app.route("/attire")
def get_attire():
  return jsonify(service.get_attire())