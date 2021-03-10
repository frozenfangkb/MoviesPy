from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
import json

with open('mongoConfig.json') as f:
    config = json.load(f)

app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = config

initialize_db(app)
initialize_routes(api)

app.run()
