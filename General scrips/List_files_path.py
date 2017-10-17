__author__ = 'Robin Cole'
__version__ = '0.1.0'
"""
Created on Tue Sep  6 10:14:30 2016
http://tkinter.unpythonic.net/wiki/tkFileDialog
"""
import os
try:
    # Python 3.x
    from tkinter import Tk
    from tkinter.filedialog import askdirectory
except ImportError:
    # Python 2.x
    from Tkinter import Tk
    from tkFileDialog import askdirectory

root = Tk().withdraw()     # Close the root window
my_dir = askdirectory()  # get directory
print(my_dir)
# my_dir = "/Users/directory_path"

f = open("file_list.txt","a") #opens file with name of "file_list.txt", creates if doesnt exist

for file in os.listdir(my_dir):
   # print(os.path.join(my_path, file))
    f.write(os.path.join(my_dir, file))
    f.write("\n")
f.close()
