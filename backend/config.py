#contains the main configuration of the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS     #Cross Origin Request - allows us to send a request to this backend from a different URL

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)    #creates a database instance which gives us access to the database specified above
