from flask import Flask, render_template, redirect, request, url_for
import smtplib
import os


my_email = os.environ.get("YOUR_EMAIL")
password = os.environ.get("PASSWORD")
print(my_email, password)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    send_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\n Phone: {phone}\n Message: {message}"
    print(send_message)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(my_email, password)
        server.sendmail(from_addr=my_email, to_addrs=email, msg=send_message)


if __name__ == "__main__":
    app.run(debug=True)
