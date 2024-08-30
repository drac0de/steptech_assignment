from flask import Flask, render_template, request, redirect, url_for, abort
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="users"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)