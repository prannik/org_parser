import scrapy
from scrapy_parser.geo_script import geo_location


class SantaelenaSpider(scrapy.Spider):
    name = 'santaelena'
    allowed_host = ['santaelena.com.co']
    start_urls = [
        'https://www.santaelena.com.co/tiendas-pasteleria/',
    ]

    def parse(self, response, **kwargs):
        data_id = response.xpath('//section[@data-id="8a22020"]/div[1]/div/div/@data-id').getall()
        for data in data_id:
            org_link = response.xpath(f'//div[@data-id="{data}"]//a//@href').get()

            yield response.follow(org_link, callback=self.parse_oragnization)

    def parse_oragnization(self, response):

        for section in response.xpath('//section/@data-id').getall()[5:-2]:
            for colum in response.xpath(f'//section[@data-id="{section}"]/div[1]/div/div/@data-id').getall():
                name = list(response.xpath(f'//div[@data-id="{colum}"]//h3/text()').getall())
                name = ''.join(name)

                if name == '':
                    continue
                if '\n' in name:
                    name = name.replace('\n', '')
                data = (
                    response.xpath(f'//div[@data-id="{colum}"]//div[@class="elementor-widget-container"]/div[@class="elementor-text-editor elementor-clearfix"]/p/text()').getall())

                data = [i.strip() for i in data]
                if data[2] == ':' or data[2] == 'Teléfono:':
                    address = data[1]
                    phones = [data[3],]
                    working_hours = data[5:]
                elif data[3] == ':' or data[3] == 'Teléfono:':
                    address = f'{data[2]} {data[3]}'
                    phones = [data[4],]
                    working_hours = data[6:]
                else:
                    address = response.xpath(
                        f'//div[@data-id="{colum}"]//div[@class="elementor-widget-container"]/div[@class="elementor-text-editor elementor-clearfix"]/p[1]/text()').getall()[0]
                    phones = response.xpath(
                        f'//div[@data-id="{colum}"]//div[@class="elementor-widget-container"]/div[@class="elementor-text-editor elementor-clearfix"]/p[2]/text()').getall()
                    working_hours = response.xpath(
                        f'//div[@data-id="{colum}"]//div[@class="elementor-widget-container"]/div[@class="elementor-text-editor elementor-clearfix"]/p[3]/text()').getall()

                city = response.xpath('//h2/text()').getall()[0].split(' ')[-1]
                latlon = geo_location.lat_long_via_address(address)
                yield {
                    'name': f'Pastelería Santa Elena {name}',
                    'address': f'{city}, {address}',
                    'latlon': latlon,
                    'phones': phones,
                    'working_hours': working_hours,
                }
