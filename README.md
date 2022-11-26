# Big data by web scraping with scrapy

On this project repository. This is where you can see the project which has been organized for collecting data as much as large scale system and being presented as charts with cutting-edge technologies at the moment.

Given that the Data Science covers many topics about how to handle data and beside its is a multi-disciplinary profession. I will be posting my progress, no only full projects, but projects that tackle vaious aspects of the Data Science pipeline.
## 1 Requiremnts
Once the lybraries needed to extract data are satisfied by below, the project could be built up:
````
pip install scrapy
pip install botocore

pip install selenium
apt install chromium-chromedriver
````

## 2 Toolkit
A diagram that shows the development enviroment with a toolkit as proposal.

![Scrapy vscode googlecolab jupyter copilot drawio](https://user-images.githubusercontent.com/23003922/197101333-74d73aaf-6bb1-4903-aed5-a3ff8828c4a9.png)

## 3 Pipeline for scraping
At this picture is ilustrated the process troughout how the files will be collected and storing for each provided URL.

![2 Pipeline for crawling](https://user-images.githubusercontent.com/23003922/197236447-821a2283-a365-4a03-9176-512f5eb91e1e.png)

## 4 Arquitecture of component design 
Here are presented three componentes throghourt data collect software cycle with Scrapy. Given the URL target, this is followed to find common and media files to store in AWS services such as DynamoDB for structured data (key-value) and S3 Bucket for pure documents. Also, it is shown two helping components for specific purpose. Once the data is retrieved they are ploted on tableu; wheremore, Selenium componen contain tools for clicking on dynamic JS events to download valid links of files.

![3 Arquitecture app drawio](https://user-images.githubusercontent.com/23003922/204070509-1856bca9-f38c-4733-99c5-af7b92962b8c.png)
