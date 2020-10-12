from zipfile import *
f = ZipFile('files.zip','r',ZIP_STORED)
names = f.namelist()
print(names)