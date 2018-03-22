__author__ = 'smail'
import psycopg2
import sys
db_con = psycopg2.connect(database='postgres', user='postgres', password='cisco2016')
cursor = db_con.cursor()
cursor.execute("CREATE TABLE customers (id SERIAL PRIMARY KEY, name VARCHAR ,age INTEGER);")
cursor.execute("INSERT INTO customers ( name, AGE) VALUES (%s, %s)",("leo", 26))
db_con.commit()
cursor.execute("SELECT * FROM customers")

class test(db_con.Model):
    id = db_con.Column(db_con.Integer, primary_key= True)
    name = db_con.Column(db_con.String(50))
    age = db_con.Column(db_con.Integer)
    posts = db_con.relationship("Post", backref="members")

    def __repr__(self):
        return "Id:{self.id}, Name: {self.name}, Age: {self.age}"

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "posts": self.posts,
        }

db_con.commit()