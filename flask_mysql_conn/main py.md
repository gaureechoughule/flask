from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "prathamesh@1194"
app.config["MYSQL_DB"] = "demo"

mysql = MySQL(app)


@app.route('/')
def about():
    id = 1
    first_name = "gauree"
    last_name = "choughule"
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO myconn1(id, first_name, last_name)VALUES (%s, %s, %s)", (id, first_name, last_name))
    mysql.connection.commit()
    cur.close()
    return "success"


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/