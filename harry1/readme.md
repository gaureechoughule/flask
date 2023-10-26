 pip install flask
 code from docum. -flask minimal app
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/
run => python app.py
1. app.run(debug=True, port=8000) change port or not  => by default it is 5000
2. bootstrap- to get readymade front end code
3. get bootstrap.com- index.html (copy text) then in body copy navbar text
4. copied form, table in (<div) new classes
5. <div class="container-fluid" => takes full page/width
6. <div class="container" => takes full page/width
<div class="container my-3">
   <h2>table1</h2>            => my-3-to give y-axis distance #mb-3 to give botton margine
<label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
#     => form & id should be same
# <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>  => if dont want then remove
# checkbox removed => <div class="mb-3 form-check">
#     <input type="checkbox" class="form-check-input" id="exampleCheck1">
#     <label class="form-check-label" for="exampleCheck1">Check me out</label>
#      </div>

# pip install flask-sqlalchemy  (ORM mapper)     => package to create database => flask-sqlalchemy documentation
# The SQLAlchemy SQL Toolkit and Object Relational Mapper is a comprehensive set of tools for working with databases and Python.
# from flask_sqlalchemy import sqlalchemy
# GOOGLE [SQLALCHEMY_DATABASE_URI] => copy (sqlite:////tmp/test.db)
 from flask_sqlalchemy import SQLAlchemy
 app = Flask(__name__[)
 app]().config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_test.db"
 db = SQLAlchemy(app)

#on terminal => python >>> from app import app, db
>>> app.app_context().push()
>>> db.create_all()  => enter then it will create my_test.db file in instance
> exit() =>on terminal
> 
> google sqlite viewer and then drag n drop file my_test.db from allfiles in yellow folder => execute
> https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application => write object
   or
> https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#check-the-sqlalchemy-documentation => query the data
> from flask import Flask, render_template, url_for => url_for(for get, post)