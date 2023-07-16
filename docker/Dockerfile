ARG DOCKER_IMAGE=python:3.6.15-slim-bullseye

FROM $DOCKER_IMAGE

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

WORKDIR /code

RUN apt-get install -y tzdata

ENV DEBIAN_FRONTEND=noninteractive \
    LANGUAGE=C.UTF-8 \
    ANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    LC_CTYPE=C.UTF-8 \
    LC_MESSAGES=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=America/Sao_Paulo

RUN apt-get update && \ 
    # Timezone
    apt-get install -y tzdata && \ 
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get update && \
    apt install -y --no-install-recommends \
    dumb-init gcc make build-essential wget curl \
    libpq-dev libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/sharkdp/hyperfine/releases/download/v1.17.0/hyperfine_1.17.0_amd64.deb && \
    dpkg -i hyperfine_1.17.0_amd64.deb && \
    rm hyperfine_1.17.0_amd64.deb

ARG SETUPTOOLS_VERSION=65.6.0
ARG REQUIREMENTS=requirements.txt
ARG REQUIREMENTS_INTERNAL=requirements-internal.txt

COPY ./${REQUIREMENTS} .
COPY ./${REQUIREMENTS_INTERNAL} .

RUN pip install pip setuptools==${SETUPTOOLS_VERSION} --upgrade && \
    pip install --no-cache-dir -r ${REQUIREMENTS} && \
    pip install --no-cache-dir -r ${REQUIREMENTS_INTERNAL}

COPY ./entrypoint.sh .

COPY ./report.py .

ENTRYPOINT ["dumb-init", "--"]
CMD ["tail", "-f", "/dev/null"]