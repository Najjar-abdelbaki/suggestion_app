from flask import Flask, render_template, request
from msg import send
from sheety import post_new_row

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        name = data.get("name")
        email = data.get("email")
        suggestion = data.get("suggestion")


        send(name, email)
        post_new_row(name, email, suggestion)
        print(f"nj7 {data}")


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)