# Module 4: run model for 1 year 

import numpy as np
read_data(Folder_File = 'Raw_Data/forest.csv')

yCz, yd13Cz = interpolation()
Car = yCz
Car_tx = []


def pde(k, a, D, h, K, i):
    global Car
    global Car_tx
    #Car_ti1 = (Car[i] * k**2 + (D * h * Car[i+1]  -2 + D * h * Car[i]) + (D * h * Car[i-1]) + (K * h * k**2 * Car[i])) / k**2    
    Car_ti1 =  (Car[i] * k**2 + (D * h * Car[i+1] - 2 * D * h * Car[i] + D * h * Car[i-1]) + (a * Car[i-1] * k - a * Car[i] * k) - K * h * k**2 * Car[i]) / k**2 
    Car_ti1 = np.array(Car_ti1, dtype=float)
    Car_tx.append(Car_ti1)
    return 


# distance
k = 0.5

# decomposition constant 
K = 0.005

# bioturbation constant
D = 0.485

# advection Constante
a = 0.03

# input Constant Topsoil
I = 0.01

# time
h = 1



def result():
    global yCz
    for i in range(1,99,1):
            pde(k,a,D,h,K,i)
    return Car_tx

result()

print
print "OC content after one year" 
print
Car_tx= np.array(Car_tx, dtype = float)
print Car_tx

x = range(1,99,1); x = np.array(x)

x100 = range(0,100,1); x100 = np.array(x100)

fig1 = plt.figure(figsize=(8, 8), dpi=300)
plt.plot(yCz, -x100, linestyle="dashed", marker="o", color="green", label="Fitted Curve")
plt.plot(Car_tx, -x, linestyle="dashed", marker="o", color="red", label="1a")
b2 = 25 #(max(yCz) + 5)
plt.xlim(0, b2) 
plt.ylabel("depth", fontsize = 16)
plt.xlabel("C (g kg-1)", fontsize = 16)
plt.legend(loc='lower right')
fig1.suptitle(("Interpolation",plot_title), fontsize=20)
plt.show()
