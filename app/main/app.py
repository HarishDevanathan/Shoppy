from flask import Flask, render_template

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')  

@app.route('/')
def index():
    return render_template("base.html")


@app.route('/aboutus')
def aboutus():
    return render_template("aboutuspage.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

