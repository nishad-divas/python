p=input("enter a parent string")
a=input("append string:")
l=int(len(p)/2)+1
new=""
new3=""

for i in range(0,l-1):
        new+=(p[i])
        new2=new+a
for i in range(l-1,len(p)):
        new3+=(p[i])
        new4=new2+new3
print("appended string",new4)