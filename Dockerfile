FROM python:3.10-slim

# إعداد مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . .

# تثبيت الاعتمادات
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# فتح المنفذ الذي تستخدمه ريندير
EXPOSE 10000

# أمر التشغيل
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
