__author__ = 'Robin Cole'
__version__ = '0.1.0'
"""
Created on Tue Sep  6 10:14:30 2016
http://tkinter.unpythonic.net/wiki/tkFileDialog
@author: robincole
"""

try:
    # Python 3.x
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
except ImportError:
    # Python 2.x
    from Tkinter import Tk
    from tkFileDialog import askopenfilename

root = Tk().withdraw()     # Close the root window
file_path = askopenfilename()
print(file_path)
