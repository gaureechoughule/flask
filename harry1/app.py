from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)




@app.route('/')
def hello_world():
    # my_test = My_test(srno="01", name="gauree", address="thane, mumbai")
    # db.session.add(my_test)
    # db.session.commit()
    # return render_template("base.html")
    # return render_template("index1.html")
    # return render_template("index.html")
    return 'Hello, World!'



# @app.route('/show')
# def show():
#     all_test = My_test.query.all()
#     print(all_test)
#     return 'this is show'

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/about')
def about():
    return 'this is about flask'

if __name__=="__main__":
    app.run(debug=True)      # app run in debug mode [python app.py]