ARG PYTHON_VERSION=3.13.12

FROM python:${PYTHON_VERSION}-slim-bookworm AS python

# Stage 1: Build dependency wheels
FROM python AS python-build-stage

RUN apt-get update && apt-get install \
    --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./backend/requirements.txt .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    --no-cache-dir \
    --no-deps \
    -r requirements.txt

# Stage 2: Python Run stage
FROM python AS python-run-stage

ARG APP_HOME=/src
ARG APP_USER=fastapi
ARG APP_GROUP=fastapi
# Must match the host user that owns the bind-mounted source tree, otherwise the
# container cannot write to ./backend/app/logs. Override with --build-arg if your
# host uid/gid is not 1000.
ARG UID=1000
ARG GID=1000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONPATH=${APP_HOME}/backend

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo git bash-completion nano ssh \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -g ${GID} ${APP_GROUP} && \
    useradd -u ${UID} -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER}


RUN mkdir -p ${APP_HOME}/backend/app/logs && \
    chown -R ${APP_USER}:${APP_GROUP} ${APP_HOME}/backend/app/logs && \
    chmod 775 ${APP_HOME}/backend/app/logs

COPY --from=python-build-stage /usr/src/app/wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels

COPY --chown=${APP_USER}:${APP_GROUP} ./backend/docker/local/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/docker/local/fastapi/start.sh /start.sh

RUN sed -i 's/\r$//g' /entrypoint.sh && \
    sed -i 's/\r$//g' /start.sh && \
    chmod +x /entrypoint.sh && \
    chmod +x /start.sh

COPY --chown=${APP_USER}:${APP_GROUP} . ${APP_HOME}

USER ${APP_USER}

ENTRYPOINT ["/entrypoint.sh"]
