# syntax=docker/dockerfile:1

FROM python:3.10.8-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc
RUN apt-get install -y default-libmysqlclient-dev

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
