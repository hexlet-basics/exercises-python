FROM hexletbasics/base-image

RUN apt update && apt install -y python3-venv python3-pytest python3-pip

RUN pip3 install --break-system-package flake8

RUN python3 -m venv /exercises-python/venv
RUN /exercises-python/venv/bin/pip install --upgrade pip

WORKDIR /exercises-python

COPY . .

ENV PYTHONPATH=/exercises-python/src

ENV PATH=/exercises-python/bin:$PATH
