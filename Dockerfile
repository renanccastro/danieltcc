FROM python:2.7.13-alpine
EXPOSE 9002
ENV PORT=9002

WORKDIR /app
ADD . /app
RUN apk add --no-cache --virtual=.build-deps \
  git openssh-client build-base mariadb-dev sqlite-libs sqlite-dev sqlite && pip install -r requirements.txt

ENTRYPOINT [ "python", "main.py" ]