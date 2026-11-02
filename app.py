from flask import Flask, render_template , request, jsonify
import os
from flask_mail import Mail, Message

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) 
app.config['TEMPLATES_AUTO_RELOAD'] = True
MAIL_SERVER=os.getenv('MAIL_SERVER')
MAIL_PORT=os.getenv('MAIL_PORT')
MAIL_USERNAME=os.getenv('MAIL_USERNAME')
MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
MAIL_SENDER=os.getenv('MAIL_SENDER')


print(MAIL_USERNAME)
print(MAIL_PASSWORD)

app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

app.config['MAIL_DEFAULT_SENDER'] = MAIL_SENDER
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

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



# NEW: Route to handle contact form submissions
@app.route("/send-message", methods=['POST'])
def send_message():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject', 'New Portfolio Message')
    message_body = data.get('message')

    if not name or not email or not message_body:
        return jsonify({"success": False, "error": "Missing required fields"}), 400

    try:
        msg = Message(
            subject=f"Portfolio Contact: {subject}",
            recipients=[os.getenv('MAIL_USERNAME')], # Sends email to your own configured inbox
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        )
        mail.send(msg)
        return jsonify({"success": True, "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
