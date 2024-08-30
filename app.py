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

@app.route('/users')
def users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cursor.execute("INSERT INTO users (name, email, role) VALUES (%s, %s, %s)", (name, email, role))
        db.commit()
        return redirect(url_for('users'))
    return render_template('new_user.html')

@app.route('/users/<int:id>')
def user_detail(id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    if user:
        return render_template('user_detail.html', user=user)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)