FROM python:3.12.6-alpine3.20
RUN apk add build-base
WORKDIR /sanic
COPY . .
RUN pip install -r requirements/requirements.txt
RUN python -m textblob.download_corpora
RUN python -m spacy download en_core_web_lg
EXPOSE 80
CMD ["sanic", "server:app", "--host=0.0.0.0", "--port=80", "--workers=4"]
