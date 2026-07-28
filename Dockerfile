FROM python:3.12-slim-bookworm
LABEL maintainer="tomer.klein@gmail.com"

ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PUSH_URL=""
ENV PUSH_INTERVAL=50

RUN pip3 install --no-cache-dir --upgrade pip setuptools

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app /app/

# Run as an unprivileged user
RUN useradd --create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app
USER appuser

# Liveness check: the agent runs as PID 1, verify it is still the process.
HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0 if 'app.py' in open('/proc/1/cmdline').read() else 1)"

ENTRYPOINT ["python3", "/app/app.py"]
