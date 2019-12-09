FROM python:3.6-slim

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["nameko", "run", "--config", "config.yml", "airports_service"]
CMD ["nameko", "run", "airports_service"]
