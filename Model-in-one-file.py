__author__ = 'rob'
# Module 1: Read CSV files containing C-Content and d13C ratios in all 4 Depth (5 / 20 / 45 / 80 cm) -> done

def read_data(Folder_File):
    import matplotlib.pyplot as plt
    import numpy as np
    import csv

    global depth
    global C_content
    global C_se
    global d13C
    global d13Cse

    data = csv.reader(open(Folder_File, 'rb'), delimiter=",", quotechar=' ')
    depth, C_content, C_se, d13C, d13Cse = [], [], [], [], []

    for row in data:
        depth.append(row[0])
        C_content.append(row[1])
        C_se.append(row[2])
        d13C.append(row[3])
        d13Cse.append(row[4])

    depth = np.array(depth[1:], dtype=float)
    C_content = np.array(C_content[1:], dtype=float)
    C_se = np.array(C_se[1:], dtype=float)
    d13C = np.array(d13C[1:], dtype=float)
    d13Cse = np.array(d13Cse[1:], dtype=float)

    print
    print "read data module ran successfuly with: ", Folder_File
    print
    print "depth (as float)     ", depth
    print "C_content (as float) ", C_content
    print "C_se (as float)      ", C_se
    print "d13C (as float)      ", d13C
    print "d13Cse (as float)    ", d13Cse
    print

    x = C_content
    x_error = C_se

    print

    x2 = d13C
    x_err = d13Cse

    return (depth, C_content, C_se, d13C, d13Cse)


#   example for usage given below

#read_data(Folder_File = 'Raw_Data/young_pasture.csv')
# Module 2: Interpolate C-Content & d13C Ratios on cm scale
#    Assuming: C(z) = a*np.exp(-b*x) + c  ***


from read_data import *
import matplotlib.pyplot as plt
import numpy as np
import csv

#read_data(Folder_File = 'Raw_Data/forest.csv')

plot_title = "primary forest"

depth, C_content, C_se, d13C, d13Cse = read_data(Folder_File = 'Raw_Data/forest.csv')


from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a*np.exp(-b*x) + c


def interpolation():
    global plot_title
    x = depth
    yC = C_content

    popt, pcov = curve_fit(func, x, yC)
    print
    print "interpolation module ran successfuly "
    print "further calculation assume:"
    print
    print "yCz = a * np.exp(-b*x) + c"
    print
    print "where: a = %s , b = %s, c = %s" % (popt[0], popt[1], popt[2])
    print

    a = popt[0]
    b = popt[1]
    c = popt[2]

    x100 = range(0,100,1)
    x100 = np.array(x100)

    yCz = a * np.exp(-b * x100) + c
    print yCz
    print

    fig1 = plt.figure(figsize=(8, 8), dpi=96)
    plt.plot(yCz, -x100, linestyle="dashed", marker="o", color="green", label="Fitted Curve")
    plt.errorbar(C_content, -depth , xerr=C_se, linestyle="None", marker="o", color="red", label="Original Data")
    b2 = 25 #(max(yCz) + 5)
    plt.xlim(0, b2)
    plt.ylabel("depth", fontsize = 16)
    plt.xlabel("C (g kg-1)", fontsize = 9)
    plt.legend(loc='lower right')
    fig1.suptitle(("Interpolation",plot_title), fontsize=20)
    plt.show()

    x = depth
    yd13C = d13C


    popt, pcov = curve_fit(func, x, -yd13C)
    print
    print "Assuming: yd13Cz = a * np.exp(-b*x) + c"
    print
    print "where: a = %s , b = %s, c = %s" % (popt[0], popt[1], popt[2])
    print

    a2 = popt[0]
    b2 = popt[1]
    c2 = popt[2]


    yd13Cz = a2 * np.exp(-b2 * x100) + c2
    yd13Cz = -yd13Cz

    print yd13Cz
    print

    fig2 = plt.figure(figsize=(8, 8), dpi=96)
    plt.plot(yd13Cz, -x100, linestyle="dashed", marker="o", color="blue", label="Fitted Curve")
    plt.errorbar(d13C, -depth , xerr=d13Cse, linestyle="None", marker="o", color="red", label="Original Data")
    b1 = (min(yd13Cz) -0.5)
    b2 = (max(yd13Cz) + 0.5)
    plt.xlim(b1, b2)
    plt.ylim(-100.0, 0.0)
    plt.ylabel("depth", fontsize=16)
    plt.xlabel("d13C ratio", fontsize=16)
    plt.legend(loc='upper right')
    fig2.suptitle(('Interpolation d13C',plot_title), fontsize=20)
    plt.show()
    return (yCz,yd13Cz)

yCz, yd13Cz = interpolation()

# Module 4: run model for 1 year


import numpy as np
from interpolation import *
#read_data(Folder_File = 'Raw_Data/forest.csv')

yCz, yd13Cz = interpolation()
Car = yCz
Car_tx = []

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


def pde(k, a, D, h, K, i):
    global Car
    global Car_tx
    #Car_ti1 = (Car[i] * k**2 + (D * h * Car[i+1]  -2 + D * h * Car[i]) + (D * h * Car[i-1]) + (K * h * k**2 * Car[i])) / k**2
    Car_ti1 =  (Car[i] * k**2 + (D * h * Car[i+1] - 2 * D * h * Car[i] + D * h * Car[i-1]) + (a * Car[i-1] * k - a * Car[i] * k) - K * h * k**2 * Car[i]) / k**2
    Car_ti1 = np.array(Car_ti1, dtype=float)
    Car_tx.append(Car_ti1)
    return


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

fig1 = plt.figure(figsize=(8, 8), dpi=96)
plt.plot(yCz, -x100, linestyle="dashed", marker="o", color="green", label="Fitted Curve")
plt.plot(Car_tx, -x, linestyle="dashed", marker="o", color="red", label="1a")
#plt.errorbar(C_content, -depth , xerr=C_se, linestyle="None", marker="o", color="red", label="Original Data")
b2 = 25 #(max(yCz) + 5)
plt.xlim(0, b2)
plt.ylabel("depth", fontsize = 16)
plt.xlabel("C (g kg-1)", fontsize = 16)
plt.legend(loc='lower right')
fig1.suptitle(("Interpolation",plot_title), fontsize=20)
plt.show()

