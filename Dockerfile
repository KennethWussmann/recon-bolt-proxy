FROM mitmproxy/mitmproxy:10.0.0
LABEL org.opencontainers.image.source https://github.com/KennethWussmann/recon-bolt-proxy

WORKDIR /app

ADD modify_reconbolt_useragent.py .
ADD entrypoint.sh .

EXPOSE 8080
EXPOSE 8081
EXPOSE 51820

ENTRYPOINT [ "./entrypoint.sh" ]