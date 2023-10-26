@app.route("/my_test")
def my_test_list():
    my_test = db.session.execute(db.select(My_test).order_by(My_test.name)).scalars()
    db.session.add(my_test)
    db.session.commit()
    return render_template("my_test/index1.html", my_test=my_test)
# extra from documn.

#index1 not running after sqlalchemy so new file base.html(id, content, completed)




