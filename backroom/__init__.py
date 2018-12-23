import os
from flask import Flask

def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev', #should be overriden with randon val at deploy
    DATABASE=os.path.join(app.instance_path, 'bloodborne.sqlite'),
  )

  # Determining whether to load in default config or passed in test config
  if test_config is None:
    app.config.from_pyfile('config.py', silent=True)
  else:
    app.config.from_mapping(test_config)

  # Blueprints
  from . import items
  app.register_blueprint(items.bp)
  
  # Ensure instance 
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  # Initialize database funcs
  from . import db
  db.init_app(app)

  return app