FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY wsgi.py .

RUN useradd -m appuser
USER appuser

EXPOSE 5000
# single worker: tasks are stored in memory, so multiple workers would not share data
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "wsgi:app"]
