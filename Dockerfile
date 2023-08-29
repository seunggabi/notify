FROM python:3.10.6 as app

WORKDIR /app
COPY . /app/

RUN ./sh/install.sh

CMD ./sh/start.sh
