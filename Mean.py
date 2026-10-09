import numpy as np
import matplotlib.pyplot as plt


year = []
nosmoothing = []
lowness = []
pos = 0

with open("Temperature.txt") as f:
    for line in f:
        column1, column2, column3 = line.strip().split()
        year.append(float(column1))
        nosmoothing.append(float(column2))
        lowness.append(float(column3))

    for i in year:
        if i == 1950:
            break
        pos = pos + 1

    pre = nosmoothing[:pos]
    post = nosmoothing[pos:]

    preunc =  np.std(pre)/np.sqrt(len(pre))
    
    
    print(f"The mean pre 1950 is {np.mean(pre)}")
    print(f"The mean post 1950 is {np.mean(post)}")
    print(f"The difference in the mean is {np.mean(post)-np.mean(pre)}")
    print(f"The uncertainty in the mean is {unc}")


            
plt.plot(year,nosmoothing)
plt.show()