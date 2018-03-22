from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, psycopg2

app = Flask(__name__)

#folder_path = os.path.abspath(os.path.dirname(__file__))
#app.config["SQLALCHEMY_DATABASE_URI"] = """sqlite:///{0}""".format(os.path.join(folder_path, "my_database.db"))
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#db = SQLAlchemy(app)
############# connecting to postgresql database#############
#host = "localhost"
#user = "postgres"
#passwd = "cisco2016"
#db1 = "postgres"
#connection = psycopg2.connect( host = host, user = user, password = passwd, dbname = db1 )
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)
##########################################################"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://sfgjmhdxpsgnkm:3c5f10ab09408ac89052fbac574ad7c673c3f74953cbbd4112e7351a076e5274@ec2-54-197-250-121.compute-1.amazonaws.com:5432/dat8akj5jacc9u'
#app.secret_key = 'some_secret'
db = SQLAlchemy(app)


from app import stores, dummy_data

member_store = stores.MemberStore()
post_store = stores.PostStore()
#dummy_data.seed_stores(member_store, post_store)

from app import views
from app import api