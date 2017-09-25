#########
# Script for copying specific multiple shapefile from large datasets
# to new folder and rename
# Copy, Folder creation based on path name and rename shapefiles
# Devloped by Sharad Shingade and Suman Kumar for UXO-India.
###############################

import os
import os.path
import ntpath
import shutil
import glob

###

data_dir = r"D:\#Resilient_Cities\Phase_I_output"

basepath = os.path.basename

print basepath

## All data directorries

all_data_dir =[x[0] for x in os.walk(data_dir)][1:]

#print all_data_dir
print "\n data directory %s....." %all_data_dir

for current_data_dir in all_data_dir:

    print "\n Processing %s ........." %basepath(current_data_dir)

    dirname =ntpath.basename(current_data_dir)
    print dirname
    ff = glob.glob(r"D:\#Resilient_Cities\Phase_I_output\%s\*urban_edge_t3.*" %(dirname))
    print ff
    folderpath = r"D:\#Resilient_Cities\T3\%s" %dirname
    print folderpath
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        for ft in ff:
            shutil.copy(ft,folderpath) ###
            files = os.listdir(folderpath)
            files_xlsx = [f for f in files if f[:10] == 'urban_edge']
            print files_xlsx
            for root, dir,files in os.walk(folderpath):
                for f in files_xlsx:
                    print f
                    dirname2 = ntpath.basename(root)
                    ori = root + '/'+ f
                    dest = root +'/' + dirname2 +f[-4:]
                    print dest
                    os.rename(ori,dest)
         

      




