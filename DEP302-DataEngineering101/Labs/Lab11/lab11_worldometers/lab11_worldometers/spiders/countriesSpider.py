import scrapy
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser

class CountriesspiderSpider(scrapy.Spider):
    name = "countriesSpider"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        countries = response.css('td a')
        for country in countries:
            name = country.css("::text").get()
            link = country.css("::attr(href)").get()
            yield response.follow(url=link, callback=self.parse_country, meta={"country_name": name, "link": link})

    def parse_country(self, response):
        open_in_browser(response)
        # name = response.request.meta["country_name"]
        # rows = response.css('table.table-striped.table-bordered.table-hover.table-condensed.table-list:nth-child(1) tbody tr')
        # for row in rows:
        #     year = row.css('td:nth-child(1)::text').get()
        #     population = row.css('td:nth-child(2) strong::text').get()
        #     yield {
        #         "country_name": name,
        #         "year": year,
        #         "population": population
        #     }
