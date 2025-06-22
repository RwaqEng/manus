
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/users')
def users():
    conn = sqlite3.connect('rwaq_users.db')
    c = conn.cursor()

    # جلب جميع المستخدمين
    c.execute("SELECT * FROM users")
    users = c.fetchall()

    # إنشاء قاموس يربط معرف المدير بالاسم
    c.execute("SELECT id, name FROM users")
    managers_dict = {row[0]: row[1] for row in c.fetchall()}

    # تحويل manager_id إلى اسم المدير
    users_with_manager_names = []
    for user in users:
        user = list(user)
        manager_id = user[7]
        manager_name = managers_dict.get(manager_id, None) if manager_id else None
        user.append(manager_name)  # نضيف اسم المدير في user[11]
        users_with_manager_names.append(user)

    conn.close()

    return render_template('users.html', users=users_with_manager_names, managers=[(u[0], u[1]) for u in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
