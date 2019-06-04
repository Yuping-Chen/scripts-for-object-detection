#-*- coding:utf-8-*-
#####作者：陈煜平#####
#####时间：2019/1/3#####
#####功能：实现统计目标检测文件下xml文件中标签的个数#####
#####输入：xml文件所在的路径xml_path#####
#####输出：标签列表name_list#####
import xml.etree.ElementTree as ET
import os
import os.path
def find_name_xml(xmlfile,name_list):
    tree=ET.parse(xmlfile)
    root=tree.getroot()
    for object in root.findall('object'):
        object_name=object.find('name').text
        if len(name_list)==0:
            name_list.append(object_name)
            continue
        else:
            i=1
            for name in name_list:
                if object_name==name:
                    break
                elif object_name!=name and i==len(name_list):
                    name_list.append(object_name)
                    break
                i+=1
    return name_list

name_list=[]
xml_path="/home/seeta/data/myData2/myData2/Annotations/"
#初始化name_list
xml_file=os.listdir(xml_path)
name_list=find_name_xml(os.path.join(xml_path,xml_file[0]),name_list)
#在文件夹下遍历xml文件
for name in xml_file[1:]:
    name_list=find_name_xml(os.path.join(xml_path,name),name_list)
print(name_list)
