import scrapy


class DentaliaSpider(scrapy.Spider):
    name = 'dentalia'
    allowed_host = ['dentalia.com']
    start_urls = [
        'https://dentalia.com',
    ]

    def parse(self, response):
        data_post_id = response.xpath('//div[@data-listing-id="231"]/div/@data-post-id').getall()
        for id in data_post_id:
            clinic_link = response.xpath(f'//div[@data-post-id="{id}"]//div[@class="elementor-widget-container"]/h2/a/@href').get()
            yield response.follow(clinic_link, callback=self.parse_clinics)

    def parse_clinics(self, response, **kwargs):

        # for post in response.xpath('//div[@data-listing-id="330"]/div/@data-post-id').getall():
        #     name = response.xpath(f'//div[@data-post-id="{post}"]//h3/text()').get()
        #     address =
        #     phones =
        #     working_hours =
        #     yield {
        #         'name': f'dentalia'}
        pass

# Тут я уперся в стену ввиде https://ru.paste.pics/PRUD0
# которую так и не смог сломать(
# если вам не сложно, подскажите пожалуйста как можно решить данную проблему
