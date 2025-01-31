FROM hexletbasics/base-image

# FIXME: use uv
RUN apt update && apt install -y python3-venv python3-flake8 python3-pytest
RUN python3 -m venv /exercises-python/venv
RUN /exercises-python/venv/bin/python -m ensurepip
RUN /exercises-python/venv/bin/pip install --upgrade pip

WORKDIR /exercises-python

COPY . .

ENV PYTHONPATH=/exercises-python/src

ENV PATH=/exercises-python/bin:$PATH
