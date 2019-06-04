#!/usr/bin/python
# -*- coding=utf-8 -*-


import xml.etree.ElementTree as ET
import os
import os.path
#import sys
#sys.setdefaultencoding="utf-8"
i=0
def alter_nodes_text(file,filename):
    #file=os.path.join(path,file)
    #print(file)
    tree=ET.parse(file)
    root=tree.getroot()

    #基础信息修改
    alter_list=["folder","filename","path"]
    for info in alter_list:
        node = root.find(info)
        if info=="folder":
            node.text="photo"
        if info=="filename":
            node.text="Safe_wear_{}.jpg".format(filename[:-4])
        if info == "path":
            node.text = "C:\\Users\\Public"

    node1=root.find("source")
    subNode1=node1.find("database")
    subNode1.text="Safe_wear"
    for subNode2 in node1.findall("task"):
        #subNode2 = node1.find("task")
        node1.remove(subNode2)

    hash_node=root.find("hash")
    root.remove(hash_node)

    #属性信息修改为name
    #attri_list=["AQM_yes","AQM_no","AQM_half","GZFSY_yes","GZFSY_no","GZFSY_half","GZFKZ_yes","GZFKZ_no","GZFKZ_half"]
    attri_list = ["AQM_if", "GZFSY_if", "GZFKZ_if"]
    for object in root.findall("object"):
        # if object.find("bndbox"):
        #     break
        for attri in attri_list:
            node=object.find(attri)
            if node==None:
                continue
            attri_name=node.text
            object.find("name").text=attri_name
            object.remove(node)
            #print(attri_name)

    tree.write(file,"UTF-8")
    global i
    i+=1
    print(">> %s 修改完成..."%(file))


path='./Annotations/'
for filenames in os.walk(path):
    filenames=list(filenames)
    filenames=filenames[2]
    for filename in filenames:
        if filename[-4:]==".xml":
            full_path=os.path.join(path,filename)
            alter_nodes_text(full_path,filename)
            #print("%s is done"%filename)
print(i)

#test one xml file
# path='./xml/'
# filename="1.xml"
# full_path=os.path.join(path,filename)
# alter_nodes_text(full_path,filename)
