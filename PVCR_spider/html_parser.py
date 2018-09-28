# coding=UTF-8
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = list()
        #/content_cvpr_2018/html/Das_Embodied_Question_Answering_CVPR_2018_paper.html
        link = soup.find('a',href=re.compile(r"content_cvpr_2018/html/*"))
        
        while link != None:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.append(new_full_url)
            link = link.find_next('a',href=re.compile(r"content_cvpr_2018/html/*"))

        return new_urls
    
    
    def _get_new_data(self, count, page_url, soup):
        res_data = {}
        
        #
        res_data['url'] = page_url
        res_data['id'] = count
        
        #<div id="papertitle">Embodied Question Answering</div>
        title_node = soup.find('div',id="papertitle")
        
        if title_node != None:
            res_data['title'] = title_node.get_text().lstrip()
            
        else:
            res_data['title'] = 'Title is null.'
        
        #<div id="abstract">We present a new ...</div>
        abstract_node = soup.find('div',id="abstract")
        
        if abstract_node != None:
            res_data['abstract'] = abstract_node.get_text().lstrip()
        else:
            res_data['abstract'] = 'Abstract is null.'
        
        return res_data
    
    def _parse_new_urls(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls
    
    def _parse_new_datas(self, count, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_data = self._get_new_data(count, page_url, soup)
        return new_data
    
    
    



