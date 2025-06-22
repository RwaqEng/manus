
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/users")
def users_page():
    conn = sqlite3.connect('rwaq_users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return render_template("users.html", users=users)

# باقي الدوال الخاصة بالتطبيق مثل login, register, وغيرها

if __name__ == "__main__":
    app.run(debug=True)
