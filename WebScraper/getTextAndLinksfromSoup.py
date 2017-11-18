import requests
from bs4 import BeautifulSoup
import webbrowser

search=input("Enter keyword you want to search:")
params={"q":search}
r=requests.get("https://www.bing.com/search",params=params)

soup=BeautifulSoup(r.text,"html.parser")
results=soup.find("ol",{"id":"b_results"})
links=results.findAll("li",{"class":"b_algo"})

for item in links:
    item_text=item.find("a").text
    item_href=item.find("a").attrs["href"]

    if item_href and item_text:
        print(item_text)
        print(item_href)
        print("Parent:",item.find("a").parent)
        print("Summary:",item.find("a").parent.parent.find("p").text)

        children=item.children
        for child in children:
            print(child)
            


