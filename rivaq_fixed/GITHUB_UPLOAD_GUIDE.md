# دليل رفع ملفات تطبيق رِواق إلى GitHub

## المشكلة الحالية
```
error: failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory
```

**السبب:** ملف `Dockerfile` غير موجود في مستودع GitHub

## الملفات المطلوبة للرفع

### ✅ الملفات الأساسية (يجب رفعها جميعاً)

#### 1. ملفات Docker (مطلوبة لـ Render)
- `Dockerfile` ⭐ **مهم جداً - هذا الملف المفقود**
- `.dockerignore`
- `docker-compose.yml` (اختياري للتطوير المحلي)
- `gunicorn.conf.py`

#### 2. ملفات Python الأساسية
- `app.py`
- `wsgi.py`
- `models.py`
- `extensions.py`
- `init_db.py`
- `requirements.txt` ⭐ **محدث بـ gunicorn و requests**

#### 3. ملفات البلوبرينت
- `auth.py`
- `api.py`
- `dashboard.py`
- `users.py`
- `tasks.py`
- `meetings.py`

#### 4. مجلد blueprints (مطلوب لحل مشكلة الاستيراد)
```
blueprints/
├── __init__.py
├── users.py
├── auth.py
└── api.py
```

#### 5. مجلدات الواجهة
```
templates/
├── base.html
├── login.html
├── dashboard.html
├── users.html
├── tasks.html
├── meetings.html
├── profile.html
└── ... (جميع ملفات HTML)

static/
├── css/
│   ├── style.css
│   └── enhanced.css
└── js/
    ├── app.js
    ├── charts.js
    └── profile_autosave.js
```

#### 6. ملفات النشر
- `Procfile` (إذا كان موجوداً)
- `render.yaml` (إذا كان موجوداً)
- `config.py`

## خطوات الرفع إلى GitHub

### الطريقة 1: الرفع عبر واجهة GitHub الويب

#### الخطوة 1: رفع الملفات الأساسية
1. اذهب إلى مستودع GitHub: `https://github.com/RwaqEng/manus`
2. اضغط على "Add file" → "Upload files"
3. ارفع هذه الملفات **بالضبط**:
   ```
   Dockerfile          ← الملف المفقود الأهم
   .dockerignore
   gunicorn.conf.py
   requirements.txt    ← المحدث
   app.py
   wsgi.py
   models.py
   extensions.py
   init_db.py
   ```

#### الخطوة 2: رفع مجلد blueprints
1. أنشئ مجلد جديد اسمه `blueprints`
2. ارفع داخله:
   ```
   blueprints/__init__.py
   blueprints/users.py
   blueprints/auth.py
   blueprints/api.py
   ```

#### الخطوة 3: رفع ملفات البلوبرينت
ارفع هذه الملفات في المجلد الجذر:
```
auth.py
api.py
dashboard.py
users.py
tasks.py
meetings.py
```

#### الخطوة 4: رفع مجلدات الواجهة
تأكد من وجود:
```
templates/ (مع جميع ملفات HTML)
static/css/ (مع ملفات CSS)
static/js/ (مع ملفات JavaScript)
```

### الطريقة 2: الرفع عبر Git Command Line

```bash
# 1. استنسخ المستودع
git clone https://github.com/RwaqEng/manus.git
cd manus

# 2. انسخ جميع الملفات من الحزمة المرفقة
cp -r /path/to/extracted/files/* .

# 3. أضف جميع الملفات
git add .

# 4. اعمل commit
git commit -m "Add Dockerfile and fix deployment issues"

# 5. ارفع التغييرات
git push origin main
```

## التحقق من الرفع الصحيح

### ✅ قائمة التحقق
بعد الرفع، تأكد من وجود هذه الملفات في GitHub:

```
✅ Dockerfile (في المجلد الجذر)
✅ .dockerignore
✅ requirements.txt (يحتوي على gunicorn)
✅ app.py
✅ wsgi.py
✅ models.py
✅ extensions.py
✅ blueprints/__init__.py
✅ blueprints/users.py
✅ templates/ (مجلد كامل)
✅ static/ (مجلد كامل)
```

### 🔍 فحص ملف Dockerfile
تأكد أن ملف `Dockerfile` يحتوي على:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
# ... باقي المحتوى
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:app"]
```

## بعد الرفع إلى GitHub

### 1. تحديث Render
1. اذهب إلى لوحة تحكم Render
2. اختر خدمة التطبيق
3. اضغط "Manual Deploy" أو انتظر التحديث التلقائي

### 2. إعدادات Render المطلوبة
```
Build Command: (اتركه فارغ أو pip install -r requirements.txt)
Start Command: gunicorn --config gunicorn.conf.py wsgi:app
```

### 3. متغيرات البيئة في Render
```
SECRET_KEY=rivaq-secret-key-2024-very-secure
DATABASE_URL=sqlite:///rivaq.db
FLASK_ENV=production
```

## استكشاف الأخطاء

### إذا استمر الخطأ:
1. **تأكد من وجود Dockerfile في المجلد الجذر**
2. **تحقق من أن الملف غير فارغ**
3. **تأكد من عدم وجود أخطاء إملائية في اسم الملف**

### إذا ظهرت أخطاء أخرى:
1. **خطأ الاستيراد:** تأكد من رفع مجلد `blueprints/`
2. **خطأ المتطلبات:** تأكد من رفع `requirements.txt` المحدث
3. **خطأ التشغيل:** تأكد من رفع `gunicorn.conf.py`

## الدعم
إذا واجهت أي مشاكل بعد اتباع هذه التعليمات، أرسل:
1. رابط مستودع GitHub
2. رسالة الخطأ الكاملة من Render
3. لقطة شاشة من ملفات المستودع

---
**ملاحظة مهمة:** تأكد من رفع **جميع** الملفات المذكورة أعلاه، خاصة `Dockerfile` و مجلد `blueprints/`

