
from scrapy.spiders import SitemapSpider

class FilteredSitemapSpider(SitemapSpider):
    name = 'news_spider'
    allowed_domains = ['www.bbc.com']
    sitemap_urls = ['http://localhost:8000/sitemap_bbc.xml']
#    sitemap_urls = ['https://www.bbc.com/sinhala/sitemap.xml']
    sitemap_rules = [('^(?!.*artist).*$', 'sitemap_filter')]
    

    def sitemap_filter(self, response):
#        print(response)
#        print('******')
#        for filter in response.xpath('//*[@id="page"]/div/text()').get() :
        body = response.xpath('//*[@id="page"]/div/div[2]/div/div[1]/div[1]/div[2]')
        news = ''
        for p in body.xpath('//p/text()'):  # this is wrong - gets all <p> from the whole document 
            news = news+ p.get() + ' '
        yield {
            'headline': response.xpath('//*[@id="page"]/div/div[2]/div/div[1]/div[1]/h1/text()').get(),
            'date' : response.xpath('//*[@id="page"]/div/div[2]/div/div[1]/div[1]/div[1]/div/div/div[1]/ul/li/div/text()').get(),
           # 'news' : response.xpath('//*[@id="page"]/div/div[2]/div/div[1]/div[1]/div[2]/p[1]/text()').get()
           'news' : news
            
        }
    

#response.xpath('//*[@id="post-4226"]/div[2]/div[1]/div/div[2]').get()                                                                                                                              
