FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Dependencies first, so code changes don't reinstall them.
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Admin CSS/JS into staticfiles/, served by WhiteNoise. The key only lets settings load; nothing is signed.
RUN DJANGO_SECRET_KEY=collectstatic-only python manage.py collectstatic --noinput

RUN useradd --create-home --uid 10001 app
USER app

EXPOSE 8000

# Production server. Settings come from the environment (see .env.example); .env is not in the image.
# Heroku assigns PORT; WEB_CONCURRENCY sets the worker count (3 fits a 512 MB dyno).
CMD ["sh", "-c", "exec gunicorn config.wsgi --bind 0.0.0.0:${PORT:-8000} --workers ${WEB_CONCURRENCY:-3} --access-logfile -"]
