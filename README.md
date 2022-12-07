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

![2 DataPipeline](https://user-images.githubusercontent.com/23003922/206234826-1fd85978-ef7e-4eb3-a94e-26a02778e4e3.png)

## 5 Arquitecture of component design 
Here are presented three componentes throghourt data collect software cycle with Scrapy. Given the URL target, this is followed to find common and media files to store in AWS services such as DynamoDB for structured data (key-value) and S3 Bucket for pure documents. Also, it is shown two helping components for specific purpose. Once the data is retrieved they are ploted on tableu; wheremore, Selenium componen contain tools for clicking on dynamic JS events to download valid links of files.

![3 Arquitecture app drawio](https://user-images.githubusercontent.com/23003922/204070509-1856bca9-f38c-4733-99c5-af7b92962b8c.png)

## 5 Storing
### A. Bitbucket Amazon S3
In the picture below is shown how the files are filled at distributed cloud storage by Amazon's bitbuckets. By web scraping over differents Chile's web sites this data storing is pure document database which each one has been retrieved of a variety of formats either PDF, CSV, XLS, Stata, and more.

![bitbucket s3 aws](https://user-images.githubusercontent.com/23003922/205807725-fb61a428-e1ce-4938-9db4-d3d620762562.jpeg)


## References

> BeautifulSoup: Interfaces for reliable connections to url as target.
*   [DynamoDB and the AWS SDKs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html)
*   [Boto3 and Amazon DynamoDB](https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/)
*   [DynamoDb in Python using BOTO3](https://www.analyticsvidhya.com/blog/2022/05/working-with-dynamodb-in-python-using-boto3/)

> Scrapy 
* [Google Colab tips: using both %%writefile magic and %%javascript magic in the same cell](https://stephencowchau.medium.com/google-colab-tips-using-both-writefile-magic-and-javascript-magic-in-the-same-cell-7820e508e455)
* [Scrapy - User Agents and Proxies](https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-user-agents-proxies/)
* [Scrapy - LinkExtractors](https://www.tutorialspoint.com/scrapy/scrapy_link_extractors.htm)
* [Scrapy - LinkExtractors - GitHub's Documentation](https://github.com/scrapy/scrapy/blob/master/docs/topics/link-extractors.rst)

> Selenium
*   [Selenium webdriver in colab](https://blog.devgenius.io/use-selenium-webdriver-in-google-colab-d5f2dba1d9f5)
*   [Selenium - Navigation](https://selenium-python.readthedocs.io/navigating.html?highlight=driver.find_element#drag-and-drop)

> Xpath
* [Parsing HTML with Xpath](https://scrapfly.io/blog/parsing-html-with-xpath/)
* [Scrapy - User Agents and Proxies](https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-user-agents-proxies/)
* [XPath tester](https://extendsclass.com/xpath-tester.html)
*   [XPath tester codebeautify](https://codebeautify.org/Xpath-Tester)
*   [Xpath for python: is xpath underappreciated?](https://towardsdatascience.com/xpath-for-python-89f4423415e0)
*   [Xpath examples](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/ms256086(v=vs.100)?redirectedfrom=MSDN)

> Regular expressions (RegEx)
*   [Regular-expressions](https://www.regular-expressions.info/tutorial.html)
*   [Python RegEx](https://www.w3schools.com/python/python_regex.asp)
*   [Regex Tester by language programming](https://regex101.com/r/vY6lJ4/1)
*   [Never use RegEx for web scraping](https://www.youtube.com/watch?v=z_cdzgrjERQ)

> Storing data in the cloud (AWS)
*   [AWS S3 bucket](https://docs.scrapy.org/en/latest/topics/feed-exports.html?highlight=aws#s3)
*   [Scrapy - Scrape Images into AWS S3](https://www.youtube.com/watch?v=CmIsvAYU-yk)
*   [How to add DataBase to Scrapy project](https://www.youtube.com/watch?v=cw5QtDxwTIQ)

> DynamoDB and its purposes (AWS)
*   [A one size fits all database doesn't fit anyone](https://www.allthingsdistributed.com/2018/06/purpose-built-databases-in-aws.html)
*   [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
*   [Scaling globally with the new AWS](https://www.allthingsdistributed.com/2022/08/aws-launches-middle-east-uae-region.html)

> Big Data and Data flow design: Apache NiFi & DynamoDB
*   [Processor: GetDynamoDB](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-aws-nar/1.19.0/org.apache.nifi.processors.aws.dynamodb.GetDynamoDB/index.html)
*   [Processor: PutDynamoDB](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-aws-nar/1.19.0/org.apache.nifi.processors.aws.dynamodb.PutDynamoDB/index.html)
*   [Processor: PutDynamoDBRecord](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-aws-nar/1.19.0/org.apache.nifi.processors.aws.dynamodb.PutDynamoDBRecord/index.html)
*   [Processor: DeleteDynamoDB](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-aws-nar/1.19.0/org.apache.nifi.processors.aws.dynamodb.DeleteDynamoDB/index.html)
