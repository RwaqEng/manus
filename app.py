
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/meetings')
def meetings():
    return render_template('meetings.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')

@app.route('/reset_password')
def reset_password():
    return render_template('reset_password.html')

if __name__ == '__main__':
    app.run(debug=True)
