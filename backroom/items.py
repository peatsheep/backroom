from flask import Blueprint, jsonify

bp = Blueprint('items', __name__, url_prefix='/items')

@bp.route('/hello')
def hello():
  return 'Hello!'