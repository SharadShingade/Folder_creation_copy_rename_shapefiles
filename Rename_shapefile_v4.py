#########
# Script for copying specific multiple shapefile from large datasets
# to new folder and rename
# Copy, Folder creation based on path name and rename shapefiles
# Devloped by Sharad Shingade and Suman Kumar for UXO-India.
###############################

import os.path, ntpath, shutil, glob


#####
# input raw data directory

raw_data = raw_input("Enter input workspace: ") # folder containing raw files of process urban edge generation
output_copy_file = raw_input("Enter copy and rename workspace:  ")

#raw_data = r"D:\#Python_script_devlopment\#halton_circle_generation\Input"
#output_copy_file = r"D:\#Python_script_devlopment\#halton_circle_generation\Final_input"

basepath = os.path.basename

print basepath

# all data directories #

all_raw_data = [x[0] for x in os.walk(raw_data)][1:]

# print all_raw_data

print "\n data dirctory %s ...." %all_raw_data

for current_data_dir in all_raw_data:

    print "\n processing %s...." %basepath(current_data_dir)

    dirname = ntpath.basename(current_data_dir)
    print dirname

    for xx in range(1,4):

        urban_edge = glob.glob(r"%s\%s\*urban_edge_t%d.*" %(raw_data,dirname,xx))

        print urban_edge

        folderpath = r"%s\T%d\%s" %(output_copy_file,xx,dirname)

        print folderpath
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
            for ft in urban_edge:
                shutil.copy(ft,folderpath)
                files = os.listdir(folderpath)
                files_xlsx = [f for f in files if f[:10] == 'urban_edge']
                print files_xlsx
                for root, dir, files in os.walk(folderpath):
                    for f in files_xlsx:
                        print f
                        dirname2 = ntpath.basename(root)
                        ori = root +'/'+f
                        dest = root+'/'+dirname2+f[-4:]
                        print dest
                        os.rename(ori,dest)
         

      




