from flask import Flask, render_template

app = Flask(__name__) 
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/en/stable/quickstart/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/angus",  methods=['POST', 'GET',])
def my_name():
    return "<p> Welcome Blessing.</p>"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/login")
def student_login():
    return render_template("login.html")

@app.route("/")
def web_assign():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
