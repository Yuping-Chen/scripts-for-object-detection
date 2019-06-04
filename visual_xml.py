# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os,cv2,os.path

xml_path='./Annotations/'
img_path='./JPEGImages/'
def xml_visual(xmlfile,imgfile):
    tree=ET.parse(xmlfile)
    root=tree.getroot()
    im = cv2.imread(imgfile)
    for object in root.findall('object'):
        object_name=object.find('name').text
        Xmin=int(object.find('bndbox').find('xmin').text)
        Ymin=int(object.find('bndbox').find('ymin').text)
        Xmax=int(object.find('bndbox').find('xmax').text)
        Ymax=int(object.find('bndbox').find('ymax').text)
        color = (4, 250, 7)
        cv2.rectangle(im,(Xmin,Ymin),(Xmax,Ymax),color,2)
        font = cv2.FONT_HERSHEY_SIMPLEX  
        cv2.putText(im, object_name, (Xmin,Ymin - 7), font, 0.5, (6, 230, 230), 2)
        #cv2.imshow('01',im)
        #cv2.waitKey()
    str=xmlfile.split("/")
    jpgname=str[-1]
    print "%s is done ..."%(jpgname)
    cv2.imwrite('img_res/{}.jpg'.format(jpgname[:-4]), im)

for img_file in os.listdir(img_path):
    #print img_file[:-4]
    for xml_file in os.listdir(xml_path):
        #print xml_file
        if xml_file[:-4]==img_file[:-4]:
            #print i
            xml_visual(os.path.join(xml_path,xml_file),os.path.join(img_path,img_file))
print "done..."


