from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy import Request
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.xlib.pydispatch import dispatcher
from twisted.internet import reactor
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.pipelines.images import ImagesPipeline


class HackerWayItem(Item):
    image_urls = Field()
    images = Field()

class BloggerSpider(CrawlSpider):
    name="TheHackerWay"
    start_urls=['https://thehackerway.com']
    allowed_domains=['thehackerway.com']
    #custom_setting ={
    #   'ITEM_PIPELINES' : 'scrapy.pipelines.images.ImagesPipeline',
    #   'IMAGES_STORE': '/home/bodhidharma/Escritorio/Practicas/Images/',
    #   'MEDIA_ALLOW_REDIRECTS': 'True'
    #}
    #settings = Settings()
    #settings = get_project_settings()
    #settings.set('ITEM_PIPELINES':     {'scrapy.pipelines.images.ImagesPipeline':1})
    rules = [Rule(LinkExtractor(allow=['.'], allow_domains=['thehackerway.com']), callback='parse_blog')]

def parse_blog(self, response):
    print("link parseado %s" % response.url)
    hxs = Selector(response)
    item = HackerWayItem()
    #urls = hxs.xpath("//img/@src").extract()
    #for u in urls:
    #item ['image_urls']=u
    item ['image_urls'] = hxs.xpath("//img/@src").extract()
    #item ['image_urls']=hxs.xpath("//*[@id='post-3762']/div[2]/p[24]/a/img/@src").extract()
    #item ['file_urls']=hxs.xpath("@href").extract()
    yield item
    #print (self.settings.attributes.values())
    #print (item)
    #return item # Retornando el Item.


def catch_item(sender, item, **kwargs):
    #print ("Item Extraido: ")#, item
    pass

if __name__ == '__main__':
    dispatcher.connect(catch_item, signal=signals.item_passed)
    dispatcher.connect(reactor.stop, signal=signals.spider_closed)


    spider = BloggerSpider()

    process = CrawlerProcess({
'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(spider)
    print ("\n[+] Starting scrapy engine...")
    #crawler.start()
    #reactor.run()

    process.start()
