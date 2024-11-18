import scrapy

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries =response.css('td a')
        for country in countries:
            name = country.css('::text')
            link = country.css('::attr(href)').get()
            yield {
                'name': name,
                'link': link
            }