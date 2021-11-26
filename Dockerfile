FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /webapp
WORKDIR /webapp
RUN pip install -U pip setuptools
COPY requirements.txt /webapp/
RUN pip install -r /webapp/requirements.txt
ADD . /webapp/
EXPOSE 8000
EXPOSE 3306