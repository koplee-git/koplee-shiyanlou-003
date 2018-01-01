# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
    @property
    def start_urls(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        print(url_tmpl.format(i) for i in range(1,5))
        return(url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.css('li.col-12.d-block.width-full.py-4.border-bottom.public'):
            item = ShiyanlouItem({
                    'name':course.css('div[class="d-inline-block mb-1"] h3 a::text').re_first('\s*(\w+)'),
                    'updata_time':course.css('div[class="f6 text-gray mt-2"] ::attr(datetime)').extract_first()
                    })
            print("################")
            print(item)
            print("################")
            yield item
