FROM python:3.8-slim as builder

RUN apt-get update --fix-missing \
    && apt-get install -y sudo vim postgresql-client make libpq-dev python3 python3-dev \
    python3-pip build-essential gcc gettext graphviz graphviz-dev \
    && apt-get -y autoremove && apt-get -y autoclean

#ARG USERNAME=biopark
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID
#RUN groupadd --gid ${USER_GID} ${USERNAME} && \
#    useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} && \
#    echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} && \
#    echo chmod 0440 /etc/sudoers.d/${USERNAME}

ARG PYTHONDONTWRITEBYTECODE=1
ENV PYTHONDONTWRITEBYTECODE=$PYTHONDONTWRITEBYTECODE

#ENV PATH="/home/${USERNAME}/.local/bin:$PATH"

#USER ${USERNAME}

ARG MODE
COPY ["biopark/requirements/", "docker/build.sh", "/tmp/"]
RUN sh /tmp/build.sh /tmp/

FROM builder AS biopark
WORKDIR /code
ADD . /code
EXPOSE 8000
STOPSIGNAL SIGINT
