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
