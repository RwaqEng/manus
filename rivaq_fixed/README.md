# نظام إدارة المهام - شركة رِواق للاستشارات الهندسية

نظام شامل لإدارة المهام والاجتماعات والمستخدمين مبني بـ Flask.

## المزايا

- 🔐 نظام مصادقة وصلاحيات متقدم
- 📋 إدارة المهام مع تتبع التقدم
- 🤝 إدارة الاجتماعات بنظام GROW
- 👥 إدارة المستخدمين والأقسام
- 📊 لوحة تحكم تفاعلية
- 📱 تصميم متجاوب

## التقنيات المستخدمة

- **Backend:** Flask, SQLAlchemy, Flask-Login
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (قابل للترقية لـ PostgreSQL)
- **Deployment:** Docker, Gunicorn

## التشغيل المحلي

### باستخدام Python
```bash
pip install -r requirements.txt
python app.py
```

### باستخدام Docker
```bash
docker build -t rivaq-app .
docker run -p 5000:5000 rivaq-app
```

### باستخدام Docker Compose
```bash
docker-compose up --build
```

## النشر

### Render
1. ارفع الملفات إلى GitHub
2. اربط المستودع مع Render
3. استخدم الإعدادات:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --config gunicorn.conf.py wsgi:app`

### متغيرات البيئة
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///rivaq.db
FLASK_ENV=production
```

## بيانات الدخول الافتراضية

- **المدير العام:** majed@rwaqeng.com / Maj@100200300
- **مدير التطوير:** asala.alsaaf@rwaqeng.com / 100200300@Aasala
- **نائب الرئيس:** muhanad.bk@rwaqeng.com / Muh@100200300

## بنية المشروع

```
├── app.py                 # التطبيق الرئيسي
├── wsgi.py               # نقطة دخول WSGI
├── models.py             # نماذج قاعدة البيانات
├── extensions.py         # إضافات Flask
├── blueprints/           # مجلد البلوبرينت
│   ├── users.py
│   ├── auth.py
│   └── api.py
├── auth.py              # بلوبرينت المصادقة
├── api.py               # بلوبرينت API
├── dashboard.py         # بلوبرينت لوحة التحكم
├── users.py             # بلوبرينت المستخدمين
├── tasks.py             # بلوبرينت المهام
├── meetings.py          # بلوبرينت الاجتماعات
├── templates/           # ملفات HTML
├── static/              # ملفات CSS/JS
├── Dockerfile           # تعريف صورة Docker
├── docker-compose.yml   # للتطوير المحلي
├── gunicorn.conf.py     # إعدادات الإنتاج
└── requirements.txt     # متطلبات Python
```

## المساهمة

1. Fork المشروع
2. أنشئ branch جديد (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push إلى Branch (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

## الترخيص

هذا المشروع مملوك لشركة رِواق للاستشارات الهندسية.

## الدعم

للدعم التقني، تواصل مع فريق التطوير.

