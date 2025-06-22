
import pandas as pd
import sqlite3
from werkzeug.security import generate_password_hash

# تحميل بيانات الإكسل
df = pd.read_excel('Rwaq - user.xlsx')

# الاتصال بقاعدة البيانات SQLite
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# إدخال المستخدمين
for index, row in df.iterrows():
    name = row['name']
    email = row['email']
    password = row['password']
    role = row['role']

    # تشفير كلمة المرور
    hashed_password = generate_password_hash(password)

    cursor.execute("""
        INSERT INTO users (name, email, password, role)
        VALUES (?, ?, ?, ?)
    """, (name, email, hashed_password, role))

conn.commit()
conn.close()

print("تم إدخال المستخدمين بنجاح.")
