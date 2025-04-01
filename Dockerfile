FROM hexletbasics/base-image

# Install pipx using apt to avoid externally-managed Python issues
RUN apt-get update && apt-get install -y pipx \
  && pipx ensurepath \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Update PATH
ENV PATH="/root/.local/bin:${PATH}"
ENV PATH="/exercises-python/bin:${PATH}"

RUN pipx install uv

ENV UV_PROJECT_ENVIRONMENT=/usr

WORKDIR /exercises-python

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

ENV PYTHONPATH=/exercises-python/src
