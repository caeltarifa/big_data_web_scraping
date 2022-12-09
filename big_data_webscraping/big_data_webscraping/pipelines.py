import hashlib
import boto3
from scrapy.pipelines.files import FilesPipeline
  
class BigDataWebscrapingPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        #file_name: str = request.url.split("/")[-1]
        #return file_name
        
        doc_url_hash = hashlib.shake_256(request.url.encode()).hexdigest(5)
        doc_perspective = request.url.split('/')[-1]
        domain= request.url.split('/')[2]
        file_name: str = f'{doc_url_hash}_{domain}_{doc_perspective}'

        return file_name
class DynamoDBPipeline(object):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.table = self.dynamodb.Table('big_data_webscraping')

    def process_item(self, item):
        self.table.put_item(
            Item = dict(
                item
                )
        )
        return item