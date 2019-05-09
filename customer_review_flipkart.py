from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import requests
import time

def read_file():
   file=open("file.html")
   data = file.read()
   file.close()
   return data

main_url = "https://www.flipkart.com/redmi-note-7-pro-nebula-red-64-gb/product-reviews/itmferghuf9ky6ru?pid=MOBFDXZ3UJJ7ETTE"

main_url = main_url+'&page='
url = main_url

user_agent = UserAgent()

f = open("final_review.txt", "w")

count = 0


for i in range(1,900):
   
   session = requests.Session()
   session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
  
   url=main_url
   url = url + str(i)
   print(url)
   page = session.get(url)
   soup = BeautifulSoup(page.content,'lxml')

   review = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('div',class_="qwjRop")

   review = [ tags.div.div.string for tags in review]
 
   for reviews in review:
      if( reviews ):
         f.write(reviews.encode("utf-8"))
         f.write("\n")
         count+=1

   time.sleep(2)
	
'''   head_review = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('p',class_='_2xg6Ul')


   for tags in head_review:
      print(tags.string)

   print("")
   print("")'''

'''   rating = soup.find('div',class_='_1HmYoV _35HD7C col-9-12').find_all('div',class_='hGSR34 E_uFuv')

   for ratings in rating:
      print(ratings.contents[0])'''
   

f.close()
print(count)
      
