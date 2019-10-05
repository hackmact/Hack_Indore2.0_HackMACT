"""Scrapper 1 is used to find the real time progressive solutions)
to the waste management of the predicted type of waste, it scrappes the first 10 sites
on Google for the solutions. Scrapping is made selective by scarpping only the HTML text that is in the form of
list (i.e numbers and bullets). This ensures that only the data that is available in form of list is scrapped.

RegEx are used to identify sucg expression in the complete text.(Efficiency can be improved by using optimised searching techniques)"""



from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "list of methods to reduce dry waste"
results=[]
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    results.append(j)
    print(j)

    req = Request(j, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage,"html.parser")
    list = page_soup.findAll("p")
    # print(soup.prettify(page_soup))
    for l in list:
        # print(l.text)
        print(l.text.findall(r'[0-2]+[\.][" "]?[A-Za-z]+[\.]',str)) # Any relevant method on any site will be in the form of a list thus having bullets, numberings.

