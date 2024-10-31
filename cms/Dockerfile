FROM python:3.12

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY src /app

WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]

