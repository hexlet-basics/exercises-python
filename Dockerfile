FROM hexletbasics/base-image

# Configure versions and paths up front for better caching
ARG PYTHON_VERSION=3.14

# Keep project bin in PATH (existing convention)
ENV PATH="/exercises-python/bin:${PATH}"

# Install curl and CA certs (minimal), then install uv via official script
ENV UV_INSTALL_DIR=/opt/uv
ENV PATH="${UV_INSTALL_DIR}/bin:${PATH}"
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && curl -fsSL https://astral.sh/uv/install.sh | sh \
  && ln -s ${UV_INSTALL_DIR}/* /usr/local/bin/

# Create a dedicated virtualenv managed by uv with the requested Python
ENV VIRTUAL_ENV=/opt/venv
ENV UV_PYTHON_INSTALL_DIR=${VIRTUAL_ENV}
RUN uv venv --allow-existing ${VIRTUAL_ENV} --python ${PYTHON_VERSION}

# Activate venv for subsequent steps and point uv to it for project deps
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"
ENV UV_PROJECT_ENVIRONMENT=${VIRTUAL_ENV}

WORKDIR /exercises-python

# Cache dependencies: copy manifests first, sync, then copy the rest
COPY pyproject.toml uv.lock ./
RUN uv sync --locked

COPY . .

ENV PYTHONPATH=/exercises-python/src
