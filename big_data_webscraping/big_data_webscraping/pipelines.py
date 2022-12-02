import hashlib
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