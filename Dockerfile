FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:10000", "rivaq_fixed.app:app"]

