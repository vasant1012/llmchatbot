FROM python:3.9-slim-buster

RUN set -xe && apt-get clean all && apt-get update -y && apt-get install -y vim wget elinks python3-pip openssl curl libssl-dev && rm -rf /var/lib/apt/lists/*

# arguments
ARG BLOB_CONNECTION_STR_ARG
ARG RESULTS_DATA_CONTAINER_ARG

ENV BLOB_CONNECTION_STR=$BLOB_CONNECTION_STR_ARG
ENV RESULTS_DATA_CONTAINER=$RESULTS_DATA_CONTAINER_ARG

RUN mkdir /opt/dash-ui/
WORKDIR /opt/dash-ui/

COPY requirements.txt /tmp/requirements.txt
COPY . /opt/dash-ui/

RUN pip install -r /tmp/requirements.txt && rm -f /tmp/requirements.txt && rm -f /opt/dash-ui/requirements.txt

RUN ls /opt/dash-ui/

RUN echo "This is the blob string - $BLOB_CONNECTION_STR"
RUN echo "This is the result container - $RESULTS_DATA_CONTAINER"

CMD ["python", "app.py"]
