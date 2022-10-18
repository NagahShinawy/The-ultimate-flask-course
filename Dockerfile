FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add build-base # gcc install
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py