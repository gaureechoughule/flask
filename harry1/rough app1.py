from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_test.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Flase   => use only when error comes
with app.app_context():
    db = SQLAlchemy(app)

class My_test(db.Model):
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.name} - {self.address}"

@app.route("/my_test")
def my_test_list():
    my_test = db.session.execute(db.select(My_test).order_by(My_test.name)).scalars()
    return render_template("my_test/index1.html", my_test=my_test)

@app.route('/show')
def show():
    all_test = My_test.query.all()
    print(all_test)
    return 'this is show'

if __name__=="__main__":
    app.run(debug=True)