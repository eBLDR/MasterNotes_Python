FROM python:3-onbuild

COPY . /usr/src/app

CMD ["nameko", "run", "--config", "config.yml", "airports_service"]
