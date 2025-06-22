
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    conn = sqlite3.connect('rwaq_users.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect(url_for('show_users'))

@app.route('/users')
def show_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    full_name = request.form['full_name']
    email = request.form['email']
    phone = request.form['phone']
    company = request.form['company']
    job_title = request.form['job_title']
    notes = request.form['notes']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO users (full_name, email, phone, company, job_title, notes) VALUES (?, ?, ?, ?, ?, ?)',
        (full_name, email, phone, company, job_title, notes)
    )
    conn.commit()
    conn.close()

    flash('تمت إضافة المستخدم بنجاح')
    return redirect(url_for('show_users'))

@app.route('/delete_user/<int:id>', methods=['POST'])
def delete_user(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash('تم حذف المستخدم بنجاح')
    return redirect(url_for('show_users'))

if __name__ == '__main__':
    app.run(debug=True, port=5007)
