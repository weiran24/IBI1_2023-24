import numpy as np
import matplotlib . pyplot as plt

population = np.zeros((100 , 100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1

beta = 0.3
gamma = 0.05
t = 0
while t < 100:
    infectedIndex = np.where(population==1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    infectedIndex2 = np.where(population==1)
    for i in range(len(infectedIndex2[0])):
        x = infectedIndex2[0][i]
        y = infectedIndex2[1][i]
        if population[x,y]==1:
            population[x,y]=np.random.choice(range(2),1,p=[gamma,1-gamma])[0]
    t = t +1

plt . figure ( figsize =(6 ,4) , dpi=150)
plt . imshow (population , cmap='viridis ' , interpolation='nearest')
plt.show()
