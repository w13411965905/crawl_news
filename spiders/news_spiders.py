import scrapy
from scrapy.spiders import CrawlSpider
from ..items import NewContext
from scrapy import item
class PositionSpider(scrapy.Spider):
    name = 'Position'
    start_urls = [
        
        
         'http://world.people.com.cn/',
         
         
    ]
    
    
    url_list=[]
    def parse(self, response):
        
        
        marqueue=response.css('marquee a::attr(href)').getall()
        focus_list=response.css('div.focus_list ul li a::attr(href)').getall()
        news_box=response.css('div.news_box ul li a::attr(href)').getall()
        col_href=response.css('div.img_box.bgc_gray a::attr(href)').getall()
        hd_href=response.css('div.hdNews.clearfix div h5 a::attr(href)').getall()
        pages_href=response.css('div.page_n.clearfix a::attr(href)').getall()
        ph_list=response.css('ul.ph_list li a::attr(href)').getall()
        
        news_box3=response.css('div.news_box3 div.img_1 a::attr(href)').getall()
        list_mt20=response.css('ul.list_14.mt20.list_14b li a::attr(href)').getall()
        list_mt15=response.css('ul.list_14.mt15 li a::attr(href)').getall()
        
        nav_url=response.css('div.nav ul li strong a::attr(href)').getall()
        next_page=response.css('div.ej_page1 center a::attr(href)').getall()
        list_ej=response.css('ul.list_14.list_ej li a::attr(href)').getall()
        nav_02=response.css('ul.nav_02 li a::attr(href)').getall()
        list_ph=response.css('ul.list_ph li a::attr(href)').getall()
        
        ph1_1=response.css('div.p1_1 ul li strong a::attr(href)').getall()
        paihang=response.css('ul.paihang li a::attr(href)').getall()
        
        mt15=response.css('div.pd_nav.w1000.white.mt15 a::attr(href)').getall()
        pages=response.css('div.page_n.clearfix a::attr(href)').getall()
        #
        list_14=response.css('ul.list_14.clearfix li a::attr(href)').getall()
        
        
        url2=marqueue+pages_href+nav_url+next_page+pages+mt15
        sum_href=focus_list + news_box + col_href + hd_href + ph_list+list_14+list_ej+nav_02+list_ph+news_box3+list_mt20+list_mt15+paihang+ph1_1
        self.url_list+=sum_href
        for u in url2:
            yield response.follow(u,callback=self.parse)
        for u in self.url_list:
            yield response.follow(u,callback=self.next_parse)
            

        

    def next_parse(self, response):
        
            t=response.css('span#rwb_navpath a::text').getall()
            author=response.css('div.box01 div.fl a::text').get()
            if t!=None:
                try:
                    t=t[1]
                except Exception:
                    t=t[0]              
            title=response.css('div.clearfix.w1000_320.text_title h1::text').get()
            
            text=response.css('div.box_con#rwb_zw p::text').getall()
            
            box_hot=response.css('div.clearfix.box_hot ul li a::attr(href)').getall()
            ph_list=response.css('ol.ph_list li a::attr(href)').getall()
            clearfix=response.css('ul.clearfix li a::attr(href)').getall()
        
            content=''.join(text)
            img=response.xpath('//body/div.clearfix.w1000_320.text_con/div.f1.text_con_left/div.box_con/img/@src').extract()
            next_url=box_hot+ph_list+clearfix
            self.url_list+=next_url
            item=NewContext()
            item['image_urls']=img
            item['type']=t
            item['author']=author
            item['title']=title
            item['text']=content
            yield item
                   
                   
        
    
    
       



''' #href=response.xpath('//body/div/a/@href').getall()
        marqueue=response.css('marquee a::attr(href)').getall()
        focus_list=response.css('div.focus_list ul li a::attr(href)').getall()
        news_box=response.css('div.news_box ul li a::attr(href)').getall()
        col_href=response.css('div.img_box.bgc_gray a::attr(href)').getall()
        hd_href=response.css('div.hdNews.clearfix div h5 a::attr(href)').getall()
        pages_href=response.css('div.page_n.clearfix a::attr(href)').getall()
        ph_list=response.css('ul.ph_list li a::attr(href)').getall()
        sum_href=marqueue + focus_list + news_box + col_href + hd_href + pages_href + ph_list
        self.url_list+=sum_href
        print(self.url_list)
        if self.url_list[self.i]!='':
            print("已执行一次")
            yield response.follow(self.url_list[self.i], callback=self.parse_detail)
            self.i+=1
            print(self.i)
'''
                
            
               
       
       

'''except Exception:
            try:
                href=response.xpath('//body/div/a/@href').getall()
                marqueue=response.css('marquee a::attr(href)').getall()
                print(marqueue)
                focus_list=response.css('div.focus_list ul li a ').getall()
                news_box=response.css('div.news_box ul li a').getall()
                col_href=response.css('div.img_box.bgc_gray a').getall()
                hd_href=response.css('div.hdNews.clearfix div h5 a').getall()
                pages_href=response.css('div.page_n.clearfix a').getall()
                ph_list=response.css('ul.ph_list li a').getall()
                list_14=response.css('ul.list_14.mt15 li a').getall()
                sum_href=href + marqueue + focus_list + news_box + col_href + hd_href + pages_href + ph_list + list_14
                if url_list[i]!='':
                    i+=1
                    yield response.follow(url_list[i], callback=self.parse)
            
           '''
       
                  
  
            