from flask import Flask
from flask_pymongo import PyMongo

# from .SecretKey import app
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

app = Flask(__name__)
password = os.environ.get("MONGODB_PWD")

app.config["MONGO_URI"] = f"mongodb+srv://dorlens:{password}@cluster0.wlayz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#setup the mongodb
mongodb_client =PyMongo(app)
db = mongodb_client.db



from website import routes