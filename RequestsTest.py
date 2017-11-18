import requests

params={"q":"pizza"}
r=requests.get("https://www.bing.com/search",params=params)
print("Status",r.status_code)
'''out1 = "(嘉南大圳 ㄐㄧㄚ　ㄋㄢˊ　ㄉㄚˋ　ㄗㄨㄣˋ )"'''
fobj = open("./page1.html", "w+", encoding="utf-8")
print(r.url)
print(r.encoding)
fobj.write(r.text)