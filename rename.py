import os 
import os.path

path="Annotations/"
for filenames in os.walk(path):
    filenames=filenames[2]
    for filename in filenames:
        #print(filename[29:])
        os.rename(os.path.join(path,filename),os.path.join(path,filename[29:]))