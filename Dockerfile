FROM melodyn/base-image:latest

RUN pip3 install flake8

WORKDIR /exercises-python

COPY --from=melodyn/base-image:latest /tmp/basics/common/* ./
COPY . .

ENV PYTHONPATH=/exercises-python/src
RUN ln -s $(which python3) /usr/bin/python
