from lxml import html
import requests
import math

bank_ypage = 'http://www.bangladeshyellowpages.com/search/categories:1085'
bank_ypage = requests.get(bank_ypage)
bankypage = html.fromstring(bank_ypage.content)

numberofpage = int(math.ceil(int(bankypage.xpath("//span[@class='displaying-num fl']")[0].text_content().split()[-1]) / 15.0))

base_head = 'http://www.bangladeshyellowpages.com/posts/search/page:' 
base_tail = '/categories:1085'
pageurls = [base_head + str(i) + base_tail for i in range(1, numberofpage)]

bank_names = set()

for url in pageurls:
    page = requests.get(url)
    name_page = html.fromstring(page.content)
    bank_names |= set(name_page.xpath("//dl[@class='result']/dd/h4/a/text()"))
    
print bank_names
