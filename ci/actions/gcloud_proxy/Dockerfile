FROM debian:buster

RUN apt update && apt install -y curl && \
    curl -Lo /usr/local/bin/cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 && \
    chmod +x /usr/local/bin/cloud_sql_proxy

ENTRYPOINT ["cloud_sql_proxy"]
