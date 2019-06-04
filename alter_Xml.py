#!/usr/bin/python
# -*- coding=utf-8 -*-


import xml.etree.ElementTree as ET
import os
import os.path
#import sys
#sys.setdefaultencoding="utf-8"

def alter_nodes_text(file):
    file=os.path.join(path,file)
    #print(file)
    tree=ET.parse(file)
    root=tree.getroot()

    for object in root.findall("size"):
        node=object.find("depth")
        name=node.text
        if name=='32':
            print("###")
            node.text=str(3)
    tree.write(file,"UTF-8")

path='./Annotations/'
for filenames in os.walk(path):
    filenames=list(filenames)
    filenames=filenames[2]
    for filename in filenames:
        if filename[-4:]==".xml":
            alter_nodes_text(filename)
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
