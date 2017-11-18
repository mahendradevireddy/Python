import requests
import simplejson as json

payload={"LongUrl":"https://www.example.com"}
url="https://www.googleapis.com/urlshortener/v1/url"
headers={"Content-Type": "application/json"}
r=requests.post(url,json=payload,headers=headers)
print(r.url)
print(r.text)

