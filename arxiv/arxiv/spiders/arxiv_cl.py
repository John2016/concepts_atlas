# -*- coding:utf-8 -*-
import scrapy
from arxiv.items import *
import re

class arxiv_cl_spider(scrapy.spider):
    name = 'arxivz_cl'
    allowed_domains = ['arxiv.org']
"""     year = 2019
    month = 8
    show_limit = 1000
    research_field = 'cs.CL'
    start_urls = 'https://arxiv.org/list/'+research_field+'/'+ \
        str(year-2000)+('0' if month < 10 else '')+str(month)+'?show='+str(show_limit) """
    start_urls = ['https://arxiv.org/list/cs.CL/1908?show=1000']

    def parse(self, response):
        self.logger.info('A response from %s just arrived' % response.url)

        num = response.xpath('//*[@id="dlpage"]/small[1]/text()[1]').extract()[0]

        max_index = int(re.search(r'\d+', num).group(0) )

        for index in range(1, max_index + 1):
            item = 