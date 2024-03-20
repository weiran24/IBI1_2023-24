a=8
b=6
c=3.5
d=2
e=1
f=24-a-b-c-d-e
my_dict={}
AS={"sleeping":a,"classes":b,"studying":c,"tv":d,"music":e,"other":f}
s=input("the time of activity you want to know")
if s in AS :
    print("the times is", AS[s],"hours.")
else :
    print("wrong")
