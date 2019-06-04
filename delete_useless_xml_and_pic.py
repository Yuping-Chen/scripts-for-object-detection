import os
import os.path

#picPath="./Annotations/"  #left
#xmlPath="./JPEGImages/"  


def cmp_two_path_file(srcdir,dstdir): #srcdir has one more file and output the file name or remove the file
    for srcFiles in os.walk(srcdir):
        srcLen=len(srcFiles[2])
        for srcFile in srcFiles[2]:
            i=0
            for dstFiles in os.walk(dstdir):
                dstLen=len(dstFiles[2])
                for dstFile in dstFiles[2]:
                    #print(i)
                    if srcFile[:-4]!=dstFile[:-4]:
                        i+=1
                        if i==dstLen:
                            #print(i)
                            print("%s"%(srcFile))
                            os.remove(os.path.join(srcdir,srcFile))

cmp_two_path_file("./Annotations/","./JPEGImages/")
print("##################")
cmp_two_path_file("./JPEGImages/","./Annotations/")
print("##################")
