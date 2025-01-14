from flask import Flask,render_template

app=Flask(__name__ , template_folder="../templates", static_folder="../static")

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutuspage.html")

@app.route('/login')
def login():
    return render_template("loginpage.html")


if(__name__=="__main__"):
    app.run(debug=True,port=5000)

