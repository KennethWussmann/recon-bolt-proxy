FROM mitmproxy/mitmproxy:10.0.0

WORKDIR /app

ADD modify_reconbolt_useragent.py .
ADD entrypoint.sh .

EXPOSE 8080
EXPOSE 8081
EXPOSE 51820

ENTRYPOINT [ "./entrypoint.sh" ]