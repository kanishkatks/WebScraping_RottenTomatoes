import json
import scrapy

class BarbieCritSpider(scrapy.Spider):
    name = "barbie_crit"
    allowed_domains = ["rottentomatoes.com"]
    start_urls = ["https://www.rottentomatoes.com/napi/movie/317d7155-533b-396f-8c1c-34a22e2e8ef9/reviews/all"]
    # next_page_base_url = ["after=" +[nextpage]"+ "%3D%3D&pageCount=20"]
    
    
    def parse(self, response):
        
        data = json.loads(response.body)
        yield from  data["reviews"]
       
        #try:
        page_id = data["pageInfo"]["endCursor"]
       
        if "==" in page_id:
            next_page = "?after=" + str(page_id[0:2]) + "%3D%3D&pageCount=20"
        else:
            next_page = "?after=" + str(page_id[0:3]) + "%3D&pageCount=20" 
        #except KeyError:
              #  page_id = None
            
        if page_id is not None:
                next_page = response.urljoin(next_page) 
                print(next_page)
                yield scrapy.Request(next_page, callback = self.parse)
        

      

        


