__author__ = 'Robin Cole'
__version__ = '0.1.0'
"""
Created on Wed Sep  7 10:33:49 2016
Iterate through file, print out search term and next line
@author: robincole
"""
import os
my_dir = "/Users/.../IAEA phase space files"

my_list = ['TITLE',
          # 'COORDINATE_SYSTEM_DESCRIPTION', 
           'BEAM_NAME', 
           'FIELD_SIZE',
           'NOMINAL_SSD']  # list of search terms

for file in os.listdir(my_dir):
    my_file = open(os.path.join(my_dir,file), "r")
    searchlines = my_file.readlines()    
    print("****************")
    print(file)

    for i, line in enumerate(searchlines):
        if any(word in line for word in my_list):
            for l in searchlines[i:i+3]: print l,
            print
    my_file.close()
