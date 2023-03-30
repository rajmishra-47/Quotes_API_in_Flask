from flask import Flask
import mysql.connector
import random

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Mishra*123",
  database="mybase"
)


cursor = db.cursor()

query = "SELECT * FROM pp"

cursor.execute(query)

results = cursor.fetchall()




app = Flask(__name__)

@app.route("/quotes")
def hello_world():
    a=results[int(random.random()*10)]
    return str(a)

if __name__=="__main__":
    app.run(debug=True)