FROM hexletbasics/base-image

ARG PYTHON_VERSION=3.14

ENV UV_INSTALL_DIR=/opt/uv
ENV PATH="${UV_INSTALL_DIR}/bin:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && curl -fsSL https://astral.sh/uv/install.sh | sh \
  && ln -s ${UV_INSTALL_DIR}/* /usr/local/bin/

ENV VIRTUAL_ENV=/opt/venv
RUN uv venv ${VIRTUAL_ENV} --python ${PYTHON_VERSION}

ENV PATH="${VIRTUAL_ENV}/bin:/exercises-python/bin:${PATH}"
ENV UV_PROJECT_ENVIRONMENT=${VIRTUAL_ENV}

WORKDIR /exercises-python

COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .

ENV PYTHONPATH=/exercises-python/src
