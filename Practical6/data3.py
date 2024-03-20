import numpy as np
import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7] 
cn_cities=[0.58,8.4,29.9,22.2]

uk_cities.sort()
print(uk_cities)
cn_cities.sort()
print(cn_cities)

uk_list=['string','ediinburgh','glasgow','london']
cn_list=['haining','hangzhou','beijing',shanghai]

plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.bar(uk_list,uk_cities,wdith=0.5,hatch='\\')
for a,b,i in zip(uk_list,uk_cities,range(len(uk_list))):
    plt.text(a,b+0,03,"%.2f"%uk_cities[i],ha='center',fontsize=10)
ply.title("Distribution of city sizes in the UK")
plt.xlabel("city")
plt.ylabel("population(million)")

plt.subplot(1,2,2)
plt.bar(cn_list,cn_cities,wdith=0.5,hatch='/')
for a,b,i in zip(cn_list,cn_cities,range(len(cn_list))):
    plt.text(a,b+0,03,"%.2f"%cn_cities[i],ha='center',fontsize=10)
ply.title("Distribution of city sizes in China")
plt.xlabel("city")
plt.ylabel("population(million)")
plt.show()
plt.clf()
