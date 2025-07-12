# declare the base images
FROM python:3.13.4-slim-bullseye

# commands:
    # docker buildx build -f Dockerfile -t pyapp .
    # docker run -it pyapp

    # docker buildx build -f Dockerfile -t sadat585/ai-py-app-test:latest .
    # docker push sadat585/ai-py-app-test:latest

WORKDIR /app

COPY ./src .

# RUN mkdir -p /static_folder
# COPY ./static_html /static_folder

# python -m http.server 8000
# docker run -it -p 3000:8000 pyapp
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]