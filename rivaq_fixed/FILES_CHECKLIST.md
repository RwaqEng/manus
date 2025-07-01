# قائمة مرجعية سريعة - الملفات المطلوبة للرفع

## ✅ الملفات الأساسية (يجب رفعها جميعاً)

### 🐳 ملفات Docker (الأهم)
- [ ] `Dockerfile` ⭐ **الملف المفقود - أولوية عالية**
- [ ] `.dockerignore`
- [ ] `gunicorn.conf.py`
- [ ] `docker-compose.yml` (اختياري)

### 🐍 ملفات Python الرئيسية
- [ ] `app.py`
- [ ] `wsgi.py`
- [ ] `models.py`
- [ ] `extensions.py`
- [ ] `init_db.py`
- [ ] `requirements.txt` ⭐ **محدث بـ gunicorn**

### 📁 مجلد blueprints (مطلوب لحل خطأ الاستيراد)
- [ ] `blueprints/__init__.py`
- [ ] `blueprints/users.py`
- [ ] `blueprints/auth.py`
- [ ] `blueprints/api.py`

### 🔗 ملفات البلوبرينت (في المجلد الجذر)
- [ ] `auth.py`
- [ ] `api.py`
- [ ] `dashboard.py`
- [ ] `users.py`
- [ ] `tasks.py`
- [ ] `meetings.py`

### 🎨 ملفات الواجهة
- [ ] `templates/` (مجلد كامل مع جميع ملفات HTML)
- [ ] `static/css/` (مجلد مع ملفات CSS)
- [ ] `static/js/` (مجلد مع ملفات JavaScript)

### ⚙️ ملفات الإعدادات
- [ ] `config.py`
- [ ] `Procfile` (إذا كان موجوداً)
- [ ] `render.yaml` (إذا كان موجوداً)

## 🚨 الملفات الأكثر أهمية (لا تنساها!)

1. **`Dockerfile`** - سبب الخطأ الحالي
2. **`requirements.txt`** - النسخة المحدثة
3. **مجلد `blueprints/`** - لحل خطأ الاستيراد
4. **`gunicorn.conf.py`** - للتشغيل في الإنتاج

## 🔍 كيفية التحقق بعد الرفع

1. اذهب إلى: `https://github.com/RwaqEng/manus`
2. تأكد من وجود `Dockerfile` في المجلد الجذر
3. تأكد من وجود مجلد `blueprints/` مع ملفاته
4. تأكد من أن `requirements.txt` يحتوي على `gunicorn==21.2.0`

## ⚡ خطوات سريعة للرفع

1. **ارفع `Dockerfile` أولاً** (الأهم)
2. ارفع `requirements.txt` المحدث
3. أنشئ مجلد `blueprints/` وارفع ملفاته
4. ارفع باقي الملفات
5. حدث في Render

---
**تذكير:** بعد رفع جميع الملفات، اذهب إلى Render واضغط "Manual Deploy"

