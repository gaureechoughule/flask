from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///D:/all python/venv tut/all flask/flask_sqlalchemy_conn/instance/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
#db.init_app(app)

with app.app_context():  # terminal-python => from app import db, db.create_all()
    db.create_all()

class Todo(db.Model):

    __tablename__ = "test"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    #completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<task %r>" % self.id


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #pass                            # pass gives error
        #return "hello"
        task_content = request.form["content"]
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "issue in task"

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()      # or => first()
        return render_template("index.html", tasks=tasks)
    #return "hello, world"
    #return render_template("index.html")

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "problem in deleting task"

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task_content = request.form["content"]

        try:
            db.session.commit()
            return redirect("/")
        except:
            return "issue in updating task"
    else:
        return render_template("update.html", task=task)


if __name__=="__main__":
    app.run(debug=True)                   #run=> python app.py