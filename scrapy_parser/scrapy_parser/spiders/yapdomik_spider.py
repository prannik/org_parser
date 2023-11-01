import scrapy


class YapdomikSpider(scrapy.Spider):
    name = 'yapdomik'
    allowed_host = ['omsk.yapdomik.ru']
    start_urls = [
        'https://omsk.yapdomik.ru',
    ]

    def parse(self, response):
        rest_links = [f'{response.url}/about']

        for links in response.xpath('//div[@class="city-select__list"]/a/@href').getall():
            rest_links.append(f'{links}/about')
        for link in rest_links:
            yield response.follow(link, callback=self.parse_restaurant)

    def parse_restaurant(self, response):

        addres = response.xpath('//a[@class="city-select__current link link--underline"]/text()').get()
        phones = response.xpath('//*[@id="app"]/div/header/div[2]/div[2]/a/text()').get()

        yield {
            'name': "Японский Домик",
            'address': addres,
            'phones': phones}
