# Module 2: Interpolate C-Content & d13C Ratios on cm scale
#    Assuming: C(z) = a*np.exp(-b*x) + c  ***


from read_data import *
import matplotlib.pyplot as plt
import numpy as np
import csv
  
#read_data(Folder_File = 'Raw_Data/forest.csv')

plot_title = "primary forest" 

depth, C_content, C_se, d13C, d13Cse = read_data(Folder_File = 'Raw_Data/forest.csv')


import numpy as np
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
    plt.xlabel("C (g kg-1)", fontsize = 16)
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
