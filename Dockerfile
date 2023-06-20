# Use a base image with Python and Chrome preinstalled
FROM --platform=$BUILDPLATFORM python:3.9 AS base
WORKDIR /app
COPY . /app

# Install system dependencies for Chrome
RUN apt-get update && apt-get install -y wget gnupg2 ca-certificates

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install project dependencies using Poetry
WORKDIR /app/avpspider
RUN pip install poetry
RUN poetry install --no-interaction --no-ansi

# Set the default command to run the project
CMD ["scrapy", "crawl", "avpamerica"]