FROM python:3.7-alpine
RUN apk --update --no-cache add vim less bash curl gcc musl-dev postgresql-libs postgresql-dev \
    build-base python-dev py-pip jpeg-dev zlib-dev libffi-dev
ENV PYTHONUNBUFFERED 1
RUN mkdir /chinook
WORKDIR /chinook
COPY requirments.txt  ./
RUN pip install -r requirments.txt
COPY ./ /chinook/