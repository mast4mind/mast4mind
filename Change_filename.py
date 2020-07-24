import os
import re


folderpath = r'C:/Users/JAMES ASMAH/Desktop/Project Oxy/IMAGES 2nd batch/Trial core maths 1993/'

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)

dirlist = sorted_alphanumeric(os.listdir(folderpath))

filenumber = 1

for filename in dirlist:
    os.replace(folderpath + '\\' + filename, folderpath + '\\' + "core_maths1993_" + str(filenumber) + ".JPG")
    filenumber +=1

