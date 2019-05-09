# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent
import requests

def customer_review_flipkart(main_url):

   main_url = main_url+'&page='
   url = main_url

   user_agent = UserAgent()

   f = open("final_review.txt", "w")

   count = 0


   for i in range(1,2):
   
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

      sleep(2)
	
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


driver = webdriver.Firefox(executable_path='/home/posi2/Downloads/geckodriver')

driver.get('https://www.flipkart.com')

   # close the login window by checking 2nd button 
driver.find_element_by_xpath("(//button)[2]").click()  

driver.implicitly_wait(10)        # implicitly wait for the 10 second for loading of the website.

search_bar = driver.find_elements_by_name('q')

driver.implicitly_wait(5)   # implicitly wait for the 5 second for better view.

search_bar[0].send_keys('washing machine')

search_bar[0].submit()

driver.implicitly_wait(10) # implicitly wait for the 10 second for loading of the website.

element = driver.find_element_by_class_name("_31qSD5")

new_url_component = element.get_attribute("href")

driver.get(new_url_component)

element = driver.find_element(By.CSS_SELECTOR,".col._39LH-M").find_elements(By.TAG_NAME,"a")

final_url_component = element[-1].get_attribute("href")

driver.get(final_url_component)

sleep(10)

driver.close()

customer_review_flipkart(final_url_component)




