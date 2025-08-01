# Python bazaviy image
FROM python:3.11-slim

# App papkasi
WORKDIR /app

# Python kutubxonalarni o‘rnatamiz
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Loyihani nusxa ko‘chiramiz
COPY . .

# Django services va media papkalarini yaratamiz
RUN mkdir -p /app/services /app/media

# Port
EXPOSE 8000

# Django collectstatic (services fayllarni tayyorlab beradi)
RUN python manage.py collectstatic --noinput

# Runserver (dev uchun)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
