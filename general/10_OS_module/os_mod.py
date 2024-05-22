import sys
import os
import shutil
import glob #The glob module finds all the pathnames matching a specified pattern
print(os.getcwd())
#os.chdir(r'C:\Docker_Tutorial\Python_Learn\Py_Learn\general') # r for raw string or use \\ for single \
print (shutil.copyfile('os_mod.py', 'os_mod1.py'))
#shutil.move('/build/executables', 'installdir') # moves directory contents
print(glob.glob('*.py'))
print (f'Argumenst to the program is {sys.argv[0]}')