import scrapy

class WikihowSpider(scrapy.Spider):
    name = 'wikihowSpider'
    start_urls = ['https://www.wikihow.com/Act-Like-You%27re-Possessed']

    def parse(self, response):
        self.title = response.xpath("//h1/a/text()").extract_first()
        for imagem in response.xpath("//li/div/a/div/img/@data-src").extract():
            # print("EIIIII=TAAAAAAAAAAAAA")
            yield {
                'title': self.title,
                'url' : imagem
            }
        # 
        # for link in response.css('a.related-title::attr(href)'):
        #     yield response.follow(link, self.parse)
    #
    # def parse_author(self, response):
    #
    #     yield{
    #         'nome': response.css('h3.author-title::text').extract_first().strip()
    #         # 'nascimento': div.css('h3.author-title::text').extract_first();
    #         # 'nome': div.css('h3.author-title::text').extract_first();
    # }
