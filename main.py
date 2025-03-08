from flask import Flask, render_template, request
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
  random_number = random.randint(1, 10)
  current_only = datetime.date.today().year
  return render_template('index.html', number=random_number, year=current_only)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
  if request.method=='POST':
    name = request.form.get("username", "")
    password = request.form.get("password", "")
  return render_template("login.html")

if __name__ == "__main__":
  app.run(debug=True)
  


