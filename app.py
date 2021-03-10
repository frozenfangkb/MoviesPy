from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from resources.routes import initialize_routes
from resources.errors import errors
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.update(JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY'))

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = os.getenv('MONGODB_HOST')

initialize_db(app)
initialize_routes(api)

app.run()
