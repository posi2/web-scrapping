import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='https://codingbat.com/python'

ua = UserAgent()   # To show server that it is human request.
header = {'user-agent':ua.chrome}

page = requests.get(url, headers = header)   # request to the server

soup=BeautifulSoup(page.content,'lxml')


''' 
	<div class="floatleft"><table>
	<tbody><tr><td><div class="summ"><a href="/python/Warmup-1"><span class="h2">Warmup-1</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Simple warmup problems to get started, no loops (solutions available)<br><img src="/c1.jpg"></div>
	</td><td><div class="summ"><a href="/python/Warmup-2"><span class="h2">Warmup-2</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Medium warmup string/list problems with loops  (solutions available)<br><img src="/c1.jpg"></div>
	</td></tr>
	<tr><td><div class="summ"><a href="/python/String-1"><span class="h2">String-1</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Basic python string problems -- no loops<br><img src="/c1.jpg"></div>
	</td><td><div class="summ"><a href="/python/List-1"><span class="h2">List-1</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Basic python list problems -- no loops.<br><img src="/c1.jpg"></div>
	</td></tr>
	<tr><td><div class="summ"><a href="/python/Logic-1"><span class="h2">Logic-1</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Basic boolean logic puzzles -- if else and or not<br><img src="/c1.jpg"></div>
	</td><td><div class="summ"><a href="/python/Logic-2"><span class="h2">Logic-2</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><img src="/s1.jpg"><br>Medium boolean logic puzzles -- if else and or not<br><img src="/c1.jpg"></div>
	</td></tr>
	<tr><td><div class="summ"><a href="/python/String-2"><span class="h2">String-2</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><br>Medium python string problems -- 1 loop.<br><img src="/c1.jpg"></div>
	</td><td><div class="summ"><a href="/python/List-2"><span class="h2">List-2</span></a> <img src="/s1.jpg"><img src="/s1.jpg"><br>Medium python list problems -- 1 loop.<br><img src="/c1.jpg"></div>
	</td></tr>
	</tbody></table>
	</div><div class="floatleft"> </div><div class="floatclear"></div><p style="max-width:800px"></p><h3>Python Help</h3><ul><li><a href="/doc/python-example-code.html">Python Example Code</a></li><li><a href="/doc/python-strings.html">Python Strings</a></li><li><a href="/doc/python-lists.html">Python Lists</a></li><li><a href="/doc/python-if-boolean.html">Python If Boolean</a></li><li><a href="/doc/practice/code-badges.html">Code Badges</a></li></ul>
        
'''

tag = soup.find_all('div',class_='summ')

# The <div class='summ'> contain all the links in <a> tag and navigable string in <span>

main_url = 'https://codingbat.com'

problem_link = [main_url+tags.a['href'] for tags in tag]

problem_heading_list = [ tags.span.string for tags in tag ] 
 
for links in problem_link:
   inner_page = requests.get(links, headers = header)   # request to the server
   inner_soup=BeautifulSoup(inner_page.content,'lxml')

   inner_tag = inner_soup.find('div',class_='indent').find('table').find_all('tr')
   inner_link = [ main_url+nested_tags.td.a['href']  for nested_tags in inner_tag]
   inner_list = [ nested_tags.td.a.string  for nested_tags in inner_tag]
  
   for link in inner_link:
      
      final_page = requests.get(link, headers = header)   # request to the server
      final_soup=BeautifulSoup(final_page.content,'lxml')

      final_tag = final_soup.find('div',class_='indent')
      
      problem_statement = final_tag.table.div.string
      print(problem_statement)

      test_case = [ sibling.string for sibling in final_tag.table.div.next_siblings if sibling.string is not None]
      print(test_case)
 
    

 
  

      
   

