FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
  jq  && \
  pip install --upgrade pip \
  requests \
  websocket-client \
  python-dotenv && \
  echo `python --version`

# For Cloud Use
COPY . /app
WORKDIR /app
RUN chmod +x bin/start.sh
CMD ["bin/start.sh"]
