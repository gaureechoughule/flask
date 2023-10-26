1. pip install flask-mysqldb
********************************************
https://flask-mysql.readthedocs.io/en/stable/
https://flask-mysqldb.readthedocs.io/en/latest/
*************************************************

2. use demo;              # in practice1 mysql workbench
create table myconn1(id int primary key, first_name varchar(20), last_name varchar(10));

3. create table students(id int, name varchar(20), email varchar(10), phone int(10));

This is Python Flask CRUD Application with backend database MYSQL. 
It covers all operation that is create, read, edit and delete

main.py => to add in table[only]

app.py => to perform crud on 1. create from 5000 port or 2.readymade table data(from mysql workbench)

app1.py => sqlalchemy connection to db