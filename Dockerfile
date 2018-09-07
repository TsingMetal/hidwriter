FROM centos

WORKDIR /hidwriter

ADD . /hidwriter

RUN yum install libusb

# install pip
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

RUN pip install pyusb

EXPOSE 8080
