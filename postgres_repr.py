from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://kari:mari@localhost:5432/karidata"

db = SQLAlchemy(app)

class a_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)

if __name__ == "__main__":
    db.create_all()
