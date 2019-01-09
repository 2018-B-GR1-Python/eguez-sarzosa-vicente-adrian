import scrapy

nombre_archivo = 'book_titles.csv'

class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider'

    ## self = this
    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Guardar
        # Nombre CSS XPATH
        # Precio CSS
        # Stock XPATH
        ## Guardar en un archivo

        print(response.css('article > h3 > a::text').extract())

        ## print(response.xpath('//*[@id="default"]/div/div/div/div/section/div/ol/li/article/h3/a/text()').extract())

        print(response.xpath('//article/h3/a/text()').extract())

        ## print(response.css('title::text').extract())



