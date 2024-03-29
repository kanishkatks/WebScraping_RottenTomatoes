import scrapy
import json

class BarbieAudienceSpider(scrapy.Spider):
    name = "barbie_audience"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/napi/movie/317d7155-533b-396f-8c1c-34a22e2e8ef9/reviews/user"]

    def parse(self, response):
        
        data = json.loads(response.body)
        yield from  data["reviews"]
       
        #try:
        page_id = data["pageInfo"]["endCursor"]
       
        
        next_page = "?after=" + str(page_id) + "&pageCount=20"
      
            
        #except KeyError:
              #  page_id = None
            
        if page_id is not None:
                next_page = response.urljoin(next_page) 
                print(next_page)
                yield scrapy.Request(next_page, callback = self.parse)