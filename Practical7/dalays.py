import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir(“C:/Users/hwr/downloads/IBI/class_materials/practical7/”)
dalys_data=pd.read_csv(“dalys-rate-from-all-causes(1).csv”)
print(dalys_data.head(5))
print(dalys_data.describe()) 
print(dalys_data.iloc[0,3]) #test if it works

print(dalys_data.iloc[0:101:10,3])
#show the fourth column (the DALYs) from every 10th row
#starting from the first row, for the rst 100 rows
#show DALYs for all rows corresponding to Afghanistan.
#identify which rows to show
AFG_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='Afghanistan':
        AFG_index.append(True)
    else:
        AFG_index.append(False)
print(dalys_data.loc[AFG_index,'DALYs'])

#deal with data of China
#identify the rows of China
CN_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='China':
        CN_index.append(True)
    else:
        CN_index.append(False)
#create object "china_data"
china_data=dalys_data.loc[CN_index,:]
#calculate mean value
CN_mean_data=np.mean(china_data.loc[:,'DALYs'])
print(CN_mean_data)
#compare mean value and value in 2019
#DALYs in China in 2019 (22270.51) was less than the mean (30677.69)
#draw the plot
plt.figure(1)
plt.plot(china_data.Year,china_data.DALYs,'b+') #'b+'is a type of the point in the figure
plt.xticks(china_data.Year,rotation=-90)

#code for question.txt
UK_index=[]
for i in range (len(dalys_data)):
    if dalys_data.iloc[i,0]=='United Kingdom':
        UK_index.append(True)
    else:
        UK_index.append(False)
UK_data=dalys_data.loc[UK_index,:]
plt.figure(2)
plt.plot(UK_data.Year,UK_data.DALYs,'r+')
plt.xticks(UK_data.Year,rotation=-90)

#show the figures
plt.show()
plt.clf()
