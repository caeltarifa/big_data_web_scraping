# Big data by web scraping with scrapy

On this project you see python modules which has been organized for collecting data as much as large scale system and being presented as charts with cutting-edge technologies at the moment.

Given the Data Science, it covers many topics about how to handle data and beside its, is a multi-disciplinary subject. highlighted updates will be posting, and every step to be executed is following the DataPipeline proposed. 

Not all techniques are being develated here, but the most useful are for ilustrating concepts and tools which Biosoft exploits with.

## 1 Requirements
Once the lybraries needed to extract data are satisfied by below, the project could be built up:
````
pip install scrapy
pip install botocore

pip install selenium
apt install chromium-chromedriver
````

## 2 How to install
Dockerfile for running up the container to set the work environment up
````
docker build -t YOUR_IMAGE_NAME .
docker run -v /dev/shm:/dev/shm --shm-size=2gb -d -p 80:8080 
````
> What about containers' high performance and its setting to collect huge datasets?

## 3 Toolkit
A diagram that shows the development enviroment with a toolkit as proposal.

![Scrapy vscode googlecolab jupyter copilot drawio](https://user-images.githubusercontent.com/23003922/197101333-74d73aaf-6bb1-4903-aed5-a3ff8828c4a9.png)

## 4 DataPipeline for scraping
At this picture is ilustrated the process troughout how the files will be collected and storing for each provided URL.

![2 DataPipeline](https://user-images.githubusercontent.com/23003922/205421418-2e36d1c4-456b-4c3b-a3b5-85e09a285ba0.png)

## 5 Arquitecture of component design 
Here are presented three componentes throghourt data collect software cycle with Scrapy. Given the URL target, this is followed to find common and media files to store in AWS services such as DynamoDB for structured data (key-value) and S3 Bucket for pure documents. Also, it is shown two helping components for specific purpose. Once the data is retrieved they are ploted on tableu; wheremore, Selenium componen contain tools for clicking on dynamic JS events to download valid links of files.

![3 Arquitecture app drawio](https://user-images.githubusercontent.com/23003922/204070509-1856bca9-f38c-4733-99c5-af7b92962b8c.png)
