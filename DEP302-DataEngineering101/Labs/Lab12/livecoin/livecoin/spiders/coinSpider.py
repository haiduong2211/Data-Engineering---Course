import scrapy
# import scrapy_splash
# from scrapy_splash import SplashRequest


#USING SELENIUM 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy import Spider, Request
from scrapy.selector import Selector

class CoinSpider(Spider):
    name = 'coinSpider'
    start_urls = ['https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/']

    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, self.parse)

    def parse(self, response):
        self.driver.get(response.url)

        # Wait for the page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "filterPanelItem___2z5Gb"))
        )

        # Click on the fifth element with the class .filterPanelItem___2z5Gb
        elements = self.driver.find_elements(By.CSS_SELECTOR,".filterPanelItem___2z5Gb")
        elements[4].click()

        # Wait for the page to update after clicking
        WebDriverWait(self.driver, 5)
        sel = Selector(text=self.driver.page_source) 
        currencies = sel.css('div.ReactVirtualized__Table__row.tableRow___3EtiS')
        for currency in currencies:
            yield {
                'name': currency.css("div:nth-child(1) div::text").get(),
                'volume(24h)': currency.css("div:nth-child(2) span::text").get()
            }
        self.driver.quit()



# class CoinspiderSpider(scrapy.Spider):
#     name = "coinSpider"
#     allowed_domains = ["web.achieve.org"]
#     script = """ 
# function main(splash, args)
#     url = args.url
#     assert(splash:go(url))
#     assert(splash:wait(5))
#     rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
#     rur_tab[5]:mouse_click(2)
#     assert(splash:wait(5))
#     splash:set_viewport_full()
#     return splash:html()
# end """

    # def start_requests(self):
    #     headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    #     }
    #     yield SplashRequest(url="https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/", callback=self.parse, endpoint="execute", args={"lua_source": self.script}, headers=headers)
    # def parse(self, response):
    #     for currency in response.css(".ReactVirtualized__Table__row .tableRow___3EtiS"):

    #         yield {
    #             "currency_pair": currency.css("div:nth-child(1) div::text").get(),
    #             "volume(24h)": currency.css("div:nth-child(2) span::text").get()
    #         }
    #         print(currency.css("div:nth-child(1) div::text").get())
