FROM python:3.6-slim

RUN apt-get update && apt-get -y install netcat && apt-get clean

WORKDIR /app
COPY . ./app

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x ./run.sh

CMD ["./run.sh"]
