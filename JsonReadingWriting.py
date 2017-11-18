import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size!=0:
    old_file=open("./ages.json","r+")
    data=json.loads(old_file.read())
    print("current age is",data["age"],"After changing----")
    data["age"]=data["age"]+1
    print("current age after changing is", data["age"])

else:
    old_file=open("./ages.json","w+")
    data={"Name":"Mahi","age":22}
    print("No file found,setting default age:",data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))


