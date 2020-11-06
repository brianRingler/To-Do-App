from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datatime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.model):
    id = db.column(db.Integer, priamry_key=True)
    content = db.Column(db.string(200), nullable=False)
    completed = db.Column(db.integer, default=0)
    data_created - db.column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)