a=8
b=6
c=3.5
d=2
e=1
f=24-a-b-c-d-e
my_dict={}
AS={"sleeping":a,"classes":b,"studying":c,"tv":d,"music":e,"other":f}
import matplotlib.pyplot as plt
class_labels=["sleeping","classes","stduying","TV","music","other"]
time_week=[a,b,c,d,e,f]
IBI1_and_else=[0,0,0,0,0,0,]
plt.figure()
plt.pie(time_week,labels=class_labels,startangle=90,explode=IBI1_and_else)
plt.show()
plt.clf()
