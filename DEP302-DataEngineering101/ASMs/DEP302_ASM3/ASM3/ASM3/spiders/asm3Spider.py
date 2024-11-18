import scrapy
import re
import unidecode as uni #Use to remove Vietnamese accent
from scrapy.exceptions import CloseSpider

class Asm3spiderSpider(scrapy.Spider):
    name = "asm3Spider"
    allowed_domains = ["web.archive.org", "ncov.moh.gov.vn"]
    start_urls = ["https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian"]


    def parse(self, response):
        items = response.css("div.timeline-detail")
        for item in items:
            #Lay thong tin ve thoi gian, tong ca mac moi va du lieu de phan tich ca moi theo tung tinh thanh
            time = item.css(".timeline-head h3::text").get()
            data_count = uni.unidecode(item.css(".timeline-content p:nth-child(2)::text").get())
            data_cases = uni.unidecode(item.css(".timeline-content p:nth-child(3)::text").get())
            new_cases = re.findall(r'VE ([0-9\\.]+) CA MAC MOI', data_count)
            
            #Lay thong tin ve so ca moi theo tung tinh thanh
            if len(new_cases) >0:
                new_cases_no = new_cases[0]
                matches = re.findall(r'([^\d,(]+)\((\d+)\)', data_cases)
                result_list = []
                for match in matches:
                    city = match[0].strip()
                    for word in ['tai','va']: #loai bo cac tu tai va trong ten tinh thanh
                        if word in city:
                            city = city.split(word)[1].strip()
                    cases = int(match[1])
                    result_list.append({"city":city,"cases": cases})

                yield {
                    "time": time,
                    "new_cases": new_cases_no,
                    "city_cases": result_list}

        #Next Page
        next_page = response.css("ul.lfr-pagination-buttons li:nth-child(2) a::attr(href)").get()   
        #check if next_page is not None 
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else:
            raise CloseSpider('ket thuc')



