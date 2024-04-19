from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/data")
def data():
    conn = sqlite3.connect('C:\\app\\Students.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentInfo;")
    data_rows = cur.fetchall()
    conn.close()
    return render_template('data.html', rows=data_rows)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000) 

