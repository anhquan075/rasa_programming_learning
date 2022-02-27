FROM rasa/rasa:2.3.2-full

USER root

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
