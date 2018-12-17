from flask import Flask, jsonify
import service

app = Flask(__name__)

@app.route("/weapons")
def get_weapons():
  return jsonify(service.get_weapons())

@app.route("/attire")
def get_attire():
  return jsonify(service.get_attire())