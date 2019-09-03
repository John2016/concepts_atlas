from scrapy.spiders import CrawlSpider, Request, Rule
import scrapy

url = 'https://arxiv.org/list/cs.CL/1908?show=1000'

response = Request(url)

print(response)

num = response.xpath('//*[@id="dlpage"]/small[1]/text()[1]').extract()[0]



