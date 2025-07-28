FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .  # copies everything in backend/

EXPOSE 5000

CMD ["gunicorn", "app:create_app()", "-b", "0.0.0.0:5000", "--timeout", "120", "--workers", "2"]
