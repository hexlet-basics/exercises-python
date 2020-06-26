FROM hexletbasics/base-image:latest

RUN pip3 install flake8 asserts
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py

WORKDIR /exercises-python

COPY . .

ENV PYTHONPATH=/exercises-python/src
RUN ln -s $(which python3) /usr/bin/python
