#-*-coding:utf-8 -*-
import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanloucourse'
    def start_requests(self):
        url_tmpl='https://github.com/shiyanlou?page={}&tab=repositories'
        urls=(url_tmpl.format(i) for i in range(1,5))
        for url in urls:
            print('****************')
            print(url)
            print('****************')
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for course in response.css('li.col-12.d-block.width-full.py-4.border-bottom.public'):
            yield {
                    'name':course.css('div[class="d-inline-block mb-1"] h3 a::text').re_first('\s*(\w+)'),

                    'updata_time':course.css('div[class="f6 text-gray mt-2"] ::attr(datetime)').extract_first()
                    }


