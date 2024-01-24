import scrapy
import json

class OppenheimerCritsSpider(scrapy.Spider):
    name = "oppenheimer_crits"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/napi/movie/07d7f9a2-3fa1-342a-b6ca-27fd594e04c6/reviews/all"]

       
    def parse(self, response):
        
        data = json.loads(response.body)
        yield from  data["reviews"]
       
        page_id = data["pageInfo"]["endCursor"]
        
            

        if "==" in page_id:
            next_page = "?after=" + str(page_id[0:2]) + "%3D%3D&pageCount=20"
        else:
            next_page = "?after=" + str(page_id[0:3]) + "%3D&pageCount=20" 


        if page_id is not None:
            next_page = response.urljoin(next_page) 
            yield scrapy.Request(next_page, callback = self.parse)
        