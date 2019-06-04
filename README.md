# scripts-for-object-detection
用于目标检测的一些脚本


##  1.split_data.py
把数据划分成：test，trainval，train，val。<br>
总样本数为test+trianval，trainval样本数=train+val。<br>
## 2.rename.py
把文件夹下的所有文件进行重命名。<br>
## 3.visual_xml.py
针对pascal voc目标检测数据集格式，输入xml和图片等路径，把可视化等结果保存到指定路径，便于可视化和数据清洗。<br>
## 4.data_augment.py + xml_helper.py
针对pascal voc目标检测数据集格式进行数据增强，输入和输出都为xml和图片。<br>
## 5.delete_one_object_in_Xml.py
删除xml多余的目标，如xml中删除不需要等人像框。<br>
## 6.delete_useless_xml_and_pic.py
删除数据集中多余等xml文件和图片。<br>
## 7.find_object_num.py
实现统计目标检测文件下xml文件中标签的个数。<br>
## 8.alter_Xml.py
修改xml文件中某个标签的text值。<br>
## 9.alter_Xml_1.py
修改xml文件中一些标签等值，把带属性的xml目标检测文件进行归一化处理。<br>
