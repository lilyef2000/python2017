# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib

driver = webdriver.PhantomJS(executable_path='C:\\phantomjs\\bin\\phantomjs')
#浏览器的地址 如果是windows，应该是某个exe地址

def search(keyword):
   url_keyword = urllib.quote(keyword)
   url = "http://www.tianyancha.com/search/" + url_keyword + "?checkFrom=searchBox"
   #print(url)
   driver.get(url)
   bsObj = BeautifulSoup(driver.page_source, "html5lib")
   #print(bsObj)
   company_list = bsObj.find_all("span", attrs={"ng-bind-html": "node.name | trustHtml"})
   print company_list
   for company in company_list:
      print(company.get_text())

if __name__ == '__main__':
   search("阿里巴巴 马云")