# commands:
    # docker buildx build -f Dockerfile -t pyapp .
    # docker run -it pyapp

    # docker buildx build -f Dockerfile -t sadat585/ai-py-app-test:latest .
    # docker push sadat585/ai-py-app-test:latest

# declare the base images
FROM python:3.13.4-slim-bullseye

# host.docker.internal -> localhost
# curl -X POST -d '{"message": "Hello world"}'  -H "Content-Type: application/json" http://host.docker.internal:8080/api/chats/
RUN apt-get update && apt-get install -y curl

RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src .

# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

# python -m http.server 8000
# docker run -it -p 3000:8000 pyapp
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]