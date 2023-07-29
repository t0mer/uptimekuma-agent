FROM python:3.11
LABEL maintainer="tomer.klein@gmail.com"

ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8
ENV PUSH_URL ""
ENV PUSH_INTERVAL 50 
RUN apt update -yqq

RUN  pip3 install --upgrade pip --no-cache-dir && \
     pip3 install --upgrade setuptools --no-cache-dir

RUN mkdir /app

COPY requirements.txt /app
COPY app /app
WORKDIR /app

RUN pip3 install -r requirements.txt
 
 
ENTRYPOINT ["python3", "/app/app.py"]
