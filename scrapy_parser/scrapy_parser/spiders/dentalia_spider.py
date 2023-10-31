import scrapy


class DentaliaSpider(scrapy.Spider):
    name = 'dentalia'
    allowed_host = ['dentalia.com']
    start_urls = [
        'https://dentalia.com/clinica/',
    ]

    def parse(self, response):
        for quote in response.css('body > div.elementor.elementor-5883.elementor-location-archive > section > div > div.elementor-column.elementor-col-50.elementor-top-column.elementor-element.elementor-element-9bd8e04 > div > section.elementor-section.elementor-inner-section.elementor-element.elementor-element-c9f8bf8.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.elementor-sticky > div > div.elementor-column.elementor-col-50.elementor-inner-column.elementor-element.elementor-element-c340ea4 > div > div > div > div > div'):
            yield {
                'name': quote.xpath('/html/body/div[2]/section/div/div[2]/div/section[2]/div/div[1]/div/div/div/div/div/select.text()').getall(),

            }

