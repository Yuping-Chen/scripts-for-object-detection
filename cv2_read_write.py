import cv2
import os
import os.path

img_path="./JPEGImages"

img_files=os.listdir(img_path)
i=0
for img_name in img_files:
    print(img_name)
    if img_name[-3:]=='JPG':
        img_name1=img_name[:-3]+'jpg'
        print(">>>>>>%s"%(img_name1))
    else:
        img_name1=img_name
    file_path=os.path.join(img_path,img_name)
    if not os.path.exists("./img"):
        os.mkdir("./img")
    save_path=os.path.join("./img",img_name1)
    img=cv2.imread(file_path)
    cv2.imwrite(save_path,img)
    i+=1
print(i)
    

print("completed...")
