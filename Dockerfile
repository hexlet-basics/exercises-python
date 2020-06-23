FROM hexletbasics/base-image:latest

RUN pip3 install flake8
RUN pip3 install asserts

WORKDIR /exercises-python

COPY . .

ENV PYTHONPATH=/exercises-python/src
RUN ln -s $(which python3) /usr/bin/python
