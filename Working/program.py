'''arr=["1","2","3","4","5"]
i=0
n=5
count=0
while count<n:
    print("i value start", i)
    i = (i + 1) % n
    while arr[i]==0:
        i=i+1
    i = (i + 1) % n
    while arr[i] == 0:
        i = i + 1
    print("i value",i)
    arr[i]=0
    count+=1



for i in arr:
    print(i)'''

print("2,3")

