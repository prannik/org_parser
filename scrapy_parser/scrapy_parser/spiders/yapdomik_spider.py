import scrapy


class YapdomikSpider(scrapy.Spider):
    name = 'yapdomik'
    allowed_host = ['omsk.yapdomik.ru']
    start_urls = [
        'https://omsk.yapdomik.ru/about',
    ]

    def parse(self, response):
        for quote in response.css('#app > main > div.container.container--shops.addressList'):
            yield {
                'name': quote.css('#ul > li:nth-child(1) > span.text()').getall(),

            }

