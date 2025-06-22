
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # تحقق من صحة الدخول
        if email == 'asala.alsaaf@rwaqeng.com' and password == '123456':
            return redirect('/users')
        else:
            return render_template('login.html', error='البريد الإلكتروني أو كلمة المرور غير صحيحة')

    return render_template('login.html')


@app.route('/users')
def users():
    # عرض صفحة المستخدمين
    return render_template('users.html')
