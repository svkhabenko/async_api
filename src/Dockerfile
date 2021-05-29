FROM python:3.9

ENV DockerHOME=/home/app/src \
    PYTHONPATH=/home/app/ \
    PYTHONDONTWRITEBYTECODE=1\
    PYTHONUNBUFFERED=1
RUN env

RUN mkdir -p $DockerHOME
WORKDIR $DockerHOME

EXPOSE 8000/tcp

RUN pip install --upgrade pip && apt-get update && apt-get install libpq-dev -y
COPY ./src/requirements.txt $DockerHOME/requirements.txt

RUN pip3 install -r ./requirements.txt

COPY ./src $DockerHOME/

ENTRYPOINT ["./entrypoint.sh"]

