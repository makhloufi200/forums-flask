from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
app = Flask(__name__)

#folder_path = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = """sqlite:///{0}""".format(os.path.join(folder_path, "my_database.db"))
##app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#db = SQLAlchemy(app)

host = "localhost"
user = "postgres"
passwd = "cisco2016"
db1 = "postgres"
connection = psycopg2.connect( host = host, user = user, password = passwd, dbname = db1 )

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
from app import stores, dummy_data

member_store = stores.MemberStore()
post_store = stores.PostStore()
dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api