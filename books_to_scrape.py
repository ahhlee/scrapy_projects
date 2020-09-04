# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksToScrapeSpider(CrawlSpider):
    name = 'books_to_scrape'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        yield {
            'book_name': response.xpath("//h1/text()").get(),
            'price': response.xpath("//p[@class='price_color']/text()").get(),
            'image': response.xpath("//@src").get(),
            'description': response.xpath("//article[@class='product_page']/p/text()").get()
        }