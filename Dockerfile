FROM python:3.11
USER root

RUN apt-get update
RUN apt-get -y install locales && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8


COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt


COPY . /app



CMD ["python", "-u", "./src/main.py"]