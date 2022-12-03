FROM python:2.7.13-alpine
EXPOSE 9002
ENV PORT=9002

WORKDIR /app
ADD . /app
RUN apk add --no-cache --virtual=.build-deps \
  git openssh-client build-base mariadb-dev sqlite-libs sqlite-dev sqlite && pip install -r requirements.txt
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://0.0.0.0:9002/api/blog/posts/ || exit 1
ENTRYPOINT [ "python", "main.py" ]