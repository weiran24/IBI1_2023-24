#import necessary libariers
import numpy as np
import matplotlib . pyplot as plt
#define a function to get the data of the number of effected people
def hsh(num1):
    beta = 0.3
    gamma = 0.05
    b = []
    aa = 1
    cc = 0
    aaa = 1
    N = 10000 
    t = 0
    percentages = (100-num1)/100
    NN = int(percentages * N)
    while t < 1000:
        b.append(aaa)
        beta1 = beta * aaa / 10000
        Z = np.random.choice(range(2),NN,p=[beta1,1-beta1])#affected
        a = list(Z)
        aa = a.count(0)
        Y = np.random.choice(range(2),aaa,p=[gamma,1-gamma])#recover
        c = list(Y)
        cc = c.count(0)
        NN = NN - aa
        aa = aa - cc
        aaa = aaa + aa
        t = t + 1
    return b
#draw pictures
line1 = plt.plot(hsh(90),label = '90%')
line2 = plt.plot(hsh(70),label = '70%')
line3 = plt.plot(hsh(50),label = '50%')
line4 = plt.plot(hsh(30),label = '30%')
line5 = plt.plot(hsh(10),label = '10%')
plt.xlabel('time')
plt.ylabel('number')
plt.title("SIR model(effected)")
plt.legend()
plt.show()
