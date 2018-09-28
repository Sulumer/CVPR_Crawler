# coding=UTF-8
from PVCR_spider import html_downloader, html_outputer, html_parser, url_manager

class SpiderMain(object):
    def __init__(self):  # 初始化
        self.urls = url_manager.UrlManager() # url管理器
        self.downloader = html_downloader.HtmlDownloader() # 下载器
        self.parser = html_parser.HtmlParser() # 解析器
        self.outputer = html_outputer.Outputer() # 输出器
        
    
    def craw(self, root_url):
        count = 0
        
        #抓取CPVR论文内容链接
        print('root_url : %s'%root_url)
        html_cont = self.downloader.download(root_url)
        new_urls = self.parser._parse_new_urls(root_url, html_cont)
        self.urls.add_new_urls(new_urls)
        
#         fout = open('result.txt','w',encoding='utf-8')
#         fout.write("abstract")
        print('There are %d results.'%len(new_urls))
        #读取CPVR论文内容链接内容
        while self.urls.has_new_url():
            try:
#                 if count == 10:
#                     break
                new_url = self.urls.get_new_url()
                print('craw %d : %s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_data = self.parser._parse_new_datas(count, new_url, html_cont)
                self.outputer.collect_data(new_data)
    
                count = count + 1
            except Exception as e:
                with open("log.txt",'a') as f: 
                    f.write(str(e))
            
        self.outputer.output_result()



if __name__ == '__main__':
    root_url='http://openaccess.thecvf.com/CVPR2018.py'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)