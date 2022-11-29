# Building container with tools for web scraping project: scrapy, python3, pip3, git, selenium, chrome driver, aws s3, aws dynamodb

######## Using the latest and LTS version of Debian ########
FROM debian:stable AS builder builder-image

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y python3.10 python3.10-dev python3.10-venv python3-pip python3-wheel build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

######## Setting up the python environment as virtual environment and activating it ########
RUN python10 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installing the required python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM debian:stable AS final runner-image
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3.10 python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder-image /opt/venv /opt/venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN echo "Python version: $(python --version) has been activated"

## Install Chrome Driver
RUN apt update 
RUN apt Install -y chromium-chromedriver
RUN wget -N https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip -P /tmp/ \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver

EXPOSE 8989

######## REFERENCES ########
# https://stackoverflow.com/questions/52949505/how-to-install-chromedriver-in-a-docker-container
# https://medium.com/analytics-vidhya/python-webscraping-in-a-docker-container-aca2a386a3c0
# https://pythonspeed.com/articles/base-image-python-docker-images/
# https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
# https://docs.docker.com/engine/reference/builder/