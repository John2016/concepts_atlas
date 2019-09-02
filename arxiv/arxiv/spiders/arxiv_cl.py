# -*- coding:utf-8 -*-
import scrapy
from arxiv.items import *
import re

class arxiv_cl_spider(scrapy.spider):
    name = 'arxivz_cl'
    allowed_domains = ['arxiv.org']

    start_urls = ['https://arxiv.org/list/cs.CL/1908?show=1000']
    
    """     year = 2019
    month = 8
    show_limit = 1000
    research_field = 'cs.CL'
    start_urls = 'https://arxiv.org/list/'+research_field+'/'+ \
        str(year-2000)+('0' if month < 10 else '')+str(month)+'?show='+str(show_limit) """

    def parse(self, response):
        self.logger.info('A response from %s just arrived' % response.url)

        num = response.xpath('//*[@id="dlpage"]/small[1]/text()[1]').extract()[0]

        max_index = int(re.search(r'\d+', num).group(0) )
        ## every item in this page contain 'title', 'authors', but 'subjects','reference',and 'comments' are random
        ## so the old method would not work for the new page
        for index in range(1, max_index + 1):
            item = ArxivItem()

            title = response.xpath('//*[@id="dlpage"]/dl/dd[' + str(index) + ']/div/div[1]/text()').extract()

            title = [i.strip() for i in title]

            title = [i for i in title if i is not '']

            item['title'] = title[0]

            author = ''
            # authors' father node
            xpath_fa = '//*[@id="dlpage"]/dl/dd[' + str(index) + ']/div/div[2]//a/text()'
            author_list = response.xpath(xpath_fa).getall()

            authors = str.join('',author_list)
            item['authors'] = authors
            
            item['subjects'] = response.xpath('string(//*[@id="dlpage"]/dl/dd['+str(5)+']/div/div[5]/span[2])').extract_first()

            yield item

        yield scrapy.Request('https://arxiv.org/list/cs.CL/1908?show=1000', callback=self.parse)