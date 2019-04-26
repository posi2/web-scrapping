import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url='http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'

ua = UserAgent()   # To show server that it is human request.
header = {'user-agent':ua.chrome}

page = requests.get(url, headers = header)   # request to the server

soup=BeautifulSoup(page.content,'html.parser')


'''
	<div id="productAZResults" class='products-a-z__results' >

	<h2 class="crux-component-title products-a-z__results__header hidden-sm hidden-xs" id="alphascroll-A">
	A
	</h2><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/air-conditioners.htm" class="products-a-z__results__item">
	Air conditioners
	</a>
	</div><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/air-filters.htm" class="products-a-z__results__item">
	Air Filters
	</a>
	</div><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/air-fryers.htm" class="products-a-z__results__item">
	Air Fryers
	</a>
	</div><h2 class="crux-component-title products-a-z__results__header hidden-sm hidden-xs" id="alphascroll-B">
	B
	</h2><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/baby-bathtubs/buying-guide.htm" class="products-a-z__results__item">
	Baby bathtubs
	</a>
	</div><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/baby-food/buying-guide.htm" class="products-a-z__results__item">
	Baby food
	</a>
	</div>

	   Similarly Pattern goes upto  Y

	<h2 class="crux-component-title products-a-z__results__header hidden-sm hidden-xs" id="alphascroll-Y">
	Y
	</h2><div class="crux-body-copy">
	<a href="https://www.consumerreports.org/cro/yogurt.htm" class="products-a-z__results__item">
	Yogurt
	</a>
	</div><nav class="hidden-lg hidden-md products-a-z__nav__container" style="height: calc(-183px + 100vh);">
	<ul class="products-a-z__nav">
	<li class="products-a-z__nav__item" data-target="alphascroll-A">
	<span class="crux-label-style">A</span>
	</li>
	<li class="products-a-z__nav__item" data-target="alphascroll-B" style="">
	<span class="crux-label-style">B</span>
	</li>

	   similarly goes upto Y   

	<li class="products-a-z__nav__item" data-target="alphascroll-Y">
	<span class="crux-label-style">Y</span>
	</li>
	</ul>
	</nav>
	</div>

'''

tag = soup.find('div',class_='products-a-z__results').find_all('div')

# The Second is for all the internal div of the <div class= 'products-a-z__results'>, which further contain <a> tag. <a> tag contain navigable string and link of the product.

product_list = [ tags.a.string for tags in tag ] 

product_links = [ tags.a['href'] for tags in tag ] 

product = { tags.a.string : tags.a['href'] for tags in tag}

print(product_list)

for key,value in product.items():
   print(key,'  -->',value)
