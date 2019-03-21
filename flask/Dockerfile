FROM python:3-alpine
MAINTAINER juancra264 "juancra264@hotmail.com"
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
## Comment the followin lines when using with compose, uncomment for stand alone tests.
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["run.py"]:
