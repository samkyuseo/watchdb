from pathlib import Path
import scrapy
from scrapy_splash import SplashRequest
import os


class HodinkeeSpider(scrapy.Spider):
    name = "hodinkee"
    start_urls = ["https://shop.hodinkee.com/collections/pre-owned-watches"]
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0"

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={"wait": 8})

    def parse(self, response):
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # print(response.body)
        # print(response.css("a.pc").getall())
        with open(Path(os.getcwd()) / "data" / "lol.html", "wb+") as f:
            f.write(response.body)
            # print(response.body.css("a.pc"))
        yield {}
