
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect(url_for('users'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/users')
def users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    managers = conn.execute('SELECT id, name FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users, managers=managers)

@app.route('/api/users', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    department = request.form['department']
    join_date = request.form['join_date']
    manager_id = request.form['manager_id'] if request.form['manager_id'] else None
    password = request.form['password']

    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, email, position, department, join_date, manager_id, password) VALUES (?, ?, ?, ?, ?, ?, ?)',
                 (name, email, position, department, join_date, manager_id, password))
    conn.commit()
    conn.close()

    return jsonify({'success': True})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()

    if user:
        return jsonify({'success': True, 'user': dict(user)})
    else:
        return jsonify({'success': False, 'message': 'المستخدم غير موجود'})

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    name = request.form['name']
    email = request.form['email']
    position = request.form['position']
    department = request.form['department']
    join_date = request.form['join_date']
    manager_id = request.form['manager_id'] if request.form['manager_id'] else None

    conn = get_db_connection()
    conn.execute('''
        UPDATE users
        SET name = ?, email = ?, position = ?, department = ?, join_date = ?, manager_id = ?
        WHERE id = ?
    ''', (name, email, position, department, join_date, manager_id, user_id))
    conn.commit()
    conn.close()

    return jsonify({'success': True})

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
