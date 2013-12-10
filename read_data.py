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
    
    
    data = csv.reader(open(Folder_File,'rb'), delimiter=",", quotechar=' ')
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
    print "depth (as float)     ",depth
    print "C_content (as float) ",C_content
    print "C_se (as float)      ",C_se
    print "d13C (as float)      ",d13C
    print "d13Cse (as float)    ",d13Cse
    print

    
# activate following line for plotting data    



    #fig1 = plt.figure(figsize=(8, 8), dpi=300)
    x = C_content
    x_error = C_se
    
    #plt.plot(x, -depth, linestyle="dashed", marker="o", color="green")
    #plt.errorbar(x, -depth, xerr=x_error, linestyle="None", marker="None", color="green")
    #plt.ylim(-100.0, 0.0)
    #plt.xlim(0.0, 25)
    #plt.ylabel("depth", fontsize = 16)
    #plt.xlabel("C (g kg-1)", fontsize = 16)
    #fig1.suptitle('Measured Carbon and standard error', fontsize=18)
    #plt.show()
    
    print 
    #fig2 = plt.figure(figsize=(8, 8), dpi=300)
    x2 = d13C
    x_err = d13Cse
    
    #plt.plot(x2, -depth, linestyle="dashed", marker="o", color="red") 
    #plt.errorbar(x2, -depth, xerr=x_err, linestyle="None", marker="None", color="red")
    #b1 = (min(d13C) -0.5)
    #b2 = (max(d13C) + 1.5)
    #plt.xlim(b1, b2) 
    #plt.ylim(-100.0, 0.0)
    #plt.ylabel("depth", fontsize=16)
    #plt.xlabel("d13C ratio", fontsize=16)
    #fig2.suptitle('Measured d13C and standard error', fontsize=18)
    #plt.show()
    return(Folder_File)


#   example for usage given below

read_data(Folder_File = 'Raw_Data/young_pasture.csv')
