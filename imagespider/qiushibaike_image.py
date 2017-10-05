import requests
import re
import time

def crawl_image(image_url, image_local_path):
   r = requests.get(image_url, stream=True)
   with open(image_local_path, "wb") as f:
      f.write(r.content)

def crwal(page):
   url = "http://www.qiushibaike.com/imgrank/page/" + str(page)
   res = requests.get(url)
   content_list = re.findall("<div class=\"thumb\">(.*?)</div>", res.content.decode("utf-8"), re.S)
   for content in content_list:
      print content
      image_list = re.findall("<img src=\"(.*?)\"", content)
      for image_url in image_list:
         image_url = "http:" + image_url
         crawl_image(image_url, "./images/" + image_url.strip().split('/')[-1])
         time.sleep(1)
if __name__ == '__main__':
   crwal(2)