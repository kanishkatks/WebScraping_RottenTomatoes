import scrapy
import json

class OppenheimerAudienceSpider(scrapy.Spider):
    name = "oppenheimer_audience"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/napi/movie/07d7f9a2-3fa1-342a-b6ca-27fd594e04c6/reviews/user"]

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