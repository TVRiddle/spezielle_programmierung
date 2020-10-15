FROM python:3
RUN pip install flask
WORKDIR /usr/src/app
ADD ./src/ /usr/src/app/
CMD ["python","-u","server.py" ]