#!/usr/bin/python
# -*- coding=utf-8 -*-


import xml.etree.ElementTree as ET
import os
import os.path
#import sys
#sys.setdefaultencoding="utf-8"

def del_nodes(file):
    file=os.path.join(path,file)
    #print(file)
    tree=ET.parse(file)
    root=tree.getroot()

    for object in root.findall("object"):
        name=object.find("name").text
        if name=="people":
            root.remove(object)
        
    tree.write(file,"UTF-8")

path='./test/'
for filenames in os.walk(path):
    filenames=list(filenames)
    filenames=filenames[2]
    for filename in filenames:
        if filename[-4:]==".xml":
            del_nodes(filename)
            print("%s is done"%filename)

'''
tree=ET.parse("test1.xml")
root=tree.getroot()

for object in root.findall("object"):
    name=object.find("name").text
    if name=="people":
        root.remove(object)
    
tree.write("test1.xml")
'''
