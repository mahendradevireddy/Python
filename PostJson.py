import requests

'''mydata={"name":"mahendra.drd@gmail.com","email":"devireddy666"}
r=requests.post("https://www.w3schools.com/php/welcome.php",data=mydata)
f=open("./myfile.html","w+",encoding="utf-8")
f.write(r.text)'''

payload = (('key1', 'value1'), ('key1', 'value2'))
headers={"Content-Type": "application/json"}
r = requests.post('http://httpbin.org/post', data=payload,headers=headers)
print(headers["Content-Type"])
