from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/home.html", title="首页")


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("/login.html", title=(f"用户名：{username}，密码：{password}"))


if __name__ == "__main__":
    app.run(debug=True)
