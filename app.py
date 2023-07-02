from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/test'
db = SQLAlchemy(app)

class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    college = db.Column(db.String(100))

    def __init__(self, name, college):
        self.name = name
        self.college = college

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']

        form_data = FormData(name=name, college=college)
        db.session.add(form_data)
        db.session.commit()

    data = FormData.query.all()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
