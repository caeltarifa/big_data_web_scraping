# Building container with tools for web scraping project: scrapy, python3, pip3, git, selenium, chrome driver, aws s3, aws dynamodb

######## Using the latest and LTS version of Debian and adding user ########
FROM debian:stable AS builder-image

RUN apt-get update && \ 
    apt-get install --no-install-recommends -y python3 python3-dev python3-venv python3-pip python3-wheel build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ARG user=webscraper
ARG home=/home/$user
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home $home \
    --ingroup root \
    $user

######## Setting up the python environment as virtual environment ########
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Installing the required python packages
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM debian:stable AS runner-image
RUN apt-get update && \
    apt-get install --no-install-recommends -y python3 python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder-image /opt/venv /opt/venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN echo "Python version: $(python3 --version) has been activated"

######## Install Chrome Driver ########
RUN apt update && \ 
    apt install -y wget && \ 
    apt install -y unzip 

RUN wget -N https://chromedriver.storage.googleapis.com/108.0.5359.22/chromedriver_linux64.zip -P /tmp/ \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod +x /usr/local/bin/chromedriver
#RUN apt install chromium-chromedriver

## Install Jupyter server
RUN pip install jupyterlab


######## Activating the user system ########
USER webscraper
WORKDIR /home/webscraper


EXPOSE 8989

######## REFERENCES ########
# https://stackoverflow.com/questions/52949505/how-to-install-chromedriver-in-a-docker-container
# https://medium.com/analytics-vidhya/python-webscraping-in-a-docker-container-aca2a386a3c0
# https://pythonspeed.com/articles/base-image-python-docker-images/
# https://luis-sena.medium.com/creating-the-perfect-python-dockerfile-51bdec41f1c8
# https://docs.docker.com/engine/reference/builder/

# docker build -t YOUR_IMAGE_NAME .
# docker run -v /dev/shm:/dev/shm --shm-size=2gb -d -p 80:8080 