from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route("/")
def home():
  random_number = random.randint(1, 10)
  current_year = datetime.datetime.now()
  year_only = current_year.year
  return render_template('index.html', number=random_number, year=year_only)

if __name__ == "__main__":
  app.run(debug=True)
  
