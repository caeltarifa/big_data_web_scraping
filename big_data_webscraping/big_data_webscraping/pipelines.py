import hashlib
import boto3
from scrapy.pipelines.files import FilesPipeline

#from scrapy_dynamodb import DynamoDbPipeline

  
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

    def process_item(self, file, spider):
        self.table.put_item(
            Item = {
                'root_url': file['root_url'],
                'date': file['date'],
                'time': file['time'],
                'file_title_web': file['file_title_web'],
                'file_stored_name': file['file_stored_name'],
                'file_down_url': file['file_down_url'],
                'file_format': file['file_format'],
                'file_size': file['file_size'],
                'file_dimension': file['file_dimension'],
                'file_urls': file['file_urls'],
            }
        )
        return file 




