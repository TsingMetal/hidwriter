FROM python:2.7-slim

WORKDIR /hidwriter

ADD . /hidwriter

RUN apt-get update
RUN apt-get install libusb-1.0-0

RUN pip install pyusb

EXPOSE 8080
