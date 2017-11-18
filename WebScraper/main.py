import requests
from bs4 import BeautifulSoup
import webbrowser

search=input("Enter Search item:")
params={"q":search}
r=requests.get("https://www.bing.com/search",params=params)
soup=BeautifulSoup(r.text,"html.parser")

print(r.url)
#print(soup.prettify())

fobj = open("./page1.html", "w+", encoding="utf-8")
fobj.write(soup.prettify())
webbrowser.open("page1.html");


