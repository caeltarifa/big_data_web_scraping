# Building container with tools for web scraping project: scrapy, python3, pip3, git, selenium, chrome driver, aws s3, aws dynamodb

######## Using the latest and LTS version of Debian and adding user ########
FROM ubuntu:22.04 AS builder-image

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y python3 python3-dev python3-venv python3-pip python3-wheel build-essential && \
    apt-get clean && \
    apt-get install -y sudo && \
    rm -rf /var/lib/apt/lists/*

ARG user_name=webscraper
ARG user_passwd=123456
RUN  useradd -g root -d /home/${user_name} -s /bin/bash -p ${user_passwd} ${user_name}

######## Setting up the python environment as virtual environment ########
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

FROM ubuntu:22.04 AS runner-image
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3 python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder-image /opt/venv /opt/venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installing the required python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


RUN echo "Python version: $(python3 --version) has been activated"

######## Install Chrome Driver ########
RUN apt update && \ 
    apt install -y wget && \ 
    apt install -y unzip 

RUN apt install -y chromium-chromedriver && \
    apt install -y libnss3 

RUN wget /usr/local/bin/https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i /usr/local/bin/google-chrome-stable_current_amd64.deb; apt-get -fy install

#RUN wget -N https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_linux64.zip -P /tmp/ \
#    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
#    && rm /tmp/chromedriver_linux64.zip \
#    && chmod +x /usr/local/bin/chromedriver

## Install Jupyter server
RUN pip install jupyterlab


######## Activating the user system ########
USER root
WORKDIR /media

EXPOSE 8989

######## REFERENCES ########
# https://stackoverflow.com/questions/52949505/how-to-install-chromedriver-in-a-docker-container
# https://medium.com/analytics-vidhya/python-webscraping-in-a-docker-container-aca2a386a3c0
# https://pythonspeed.com/articles/base-image-python-docker-images/
# https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
# https://docs.docker.com/engine/reference/builder/