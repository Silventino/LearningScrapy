import scrapy

class AutoresSpider(scrapy.Spider):
    name = 'autores'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for linkToAuthor in response.css('div.quote span a::attr(href)'):
            yield response.follow(linkToAuthor, self.parse_author)

        for link in response.css('li.next a::attr(href)'):
            yield response.follow(link, self.parse)

    def parse_author(self, response):

        yield{
            'nome': response.css('h3.author-title::text').extract_first().strip()
            # 'nascimento': div.css('h3.author-title::text').extract_first();
            # 'nome': div.css('h3.author-title::text').extract_first();
        }
