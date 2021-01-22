FROM python:3-onbuild

COPY . /usr/src/app

CMD ["nameko", "run", "--config", "config.yml", "gateway_service"]
