from flask import Flask, render_template
from markupsafe import escape
import random
import datetime
import requests
from flask import url_for

app = Flask(__name__)

@app.route("/")
def home():
  random_number = random.randint(1, 10)
  current_only = datetime.date.today().year
  return render_template('index.html', number=random_number, year=current_only)

@app.route("/guess/<username>")
def guess_user(username):
  gender_response = requests.get(f"https://api.genderize.io?name={username}")
  gender_data = gender_response.json()
  gender = gender_data["gender"]
  return render_template("guess.html", name=username, gender=gender)

@app.route("/blogs")
def blog_post():
  posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
  all_posts = posts_response.json()
  return render_template("posts.html", posts=all_posts)

if __name__ == "__main__":
  app.run(debug=True)
  


