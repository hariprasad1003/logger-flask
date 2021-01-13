FROM python:3.7-alpine
RUN apk update
WORKDIR /logger_flask
ADD . /logger_flask
RUN pip install -r requirements.txt
CMD ["python3","app.py"]