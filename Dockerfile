FROM python:3

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update && apt-get install -yqq git python3-pip

RUN pip3 install yamllint
RUN pip3 install asserts

WORKDIR /exercises-python

# COPY package.json package.json
# COPY package-lock.json package-lock.json
# RUN npm install

COPY . /exercises-python
