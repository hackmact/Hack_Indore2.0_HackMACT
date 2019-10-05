"""The Scrapper2 is also made to generate the progressive solutions
It searches the google home-page for disposal techniques of the predicted
 type of waste and suggest it to the user. Scrapping can be further optimised by being
 more selective while scrapping the data."""



from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import re

waste ="dry" #will be the predicted value obtained from the model
fill="list+of+methods+to+dispose" + waste +"waste"
str = "https://www.google.com/search?sxsrf=ACYBGNS67V8caAimLsbUKme_mCfd5p6cEg%3A1570215365522&ei=xZWXXcu8H9Cw9QPinbbwDA&q=" + fill + "&oq=" + fill + "&gs_l=psy-ab.3..35i39j0i67j0l8.7169.8116..8464...0.2..0.159.756.0j5....3..0....1..gws-wiz.......0i71.3UYa_nC9F9w&ved=0ahUKEwiLs9SIpIPlAhVQWH0KHeKODc4Q4dUDCAs&uact=5"



req = Request(str, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# webpage="<div>hi<p>hello</p>bye</div>"

page_soup = soup(webpage,"html.parser")
list=page_soup.findAll("li")

for l in list:
    print(l.text)






