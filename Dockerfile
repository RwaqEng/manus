# استخدام بايثون 3.10
FROM python:3.10-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات المشروع إلى الحاوية
COPY . .

# تحديث pip وتثبيت الأدوات الأساسية
RUN pip install --upgrade pip setuptools wheel

# تثبيت المتطلبات
RUN pip install -r requirements.txt

# الأمر الذي يتم تشغيله عند بدء الخدمة
CMD ["gunicorn", "-b", "0.0.0.0:10000", "main:app"]
