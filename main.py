from flask import Flask,render_template 

app = Flask(__name__)


@app.route("/")
def  hello():
    return render_template("home.html")

@app.route("/index")
def  index():
    return render_template("index.html")

@app.route("/3Dpy")
def  play2():
    return render_template("3D-d.html")   

@app.route("/chat")
def chat():
    return render_template('chatbot.html')
@app.route("/CSS")
def Css():
    return render_template('CSS.html')
@app.route('/Build')
def build():
    return render_template('Build.html')
@app.route('/Flask')
def Flask():
    return render_template('Flask.html')
@app.route('/HTML')
def HTML():
    return render_template('HTML.html')
@app.route('/3D')
def D():
    return render_template('3D-Design.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)