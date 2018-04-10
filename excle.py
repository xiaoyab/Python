#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#新建excle文件并写入数据
import xlwt
import xlutils.copy

#对xls文件初始化
workbook = xlwt.Workbook(encoding='utf-8')

sheet_a = workbook.add_sheet(u'text1')
sheet_b = workbook.add_sheet(u'text2')
sheet_c = workbook.add_sheet(u'text3')
print (sheet_a)

fg_a = open('/Users/zhouxiaoya/learngit/Python/req.py','r')
fg_b = open('/Users/zhouxiaoya/learngit/Python/picture.py','r')
fg_c = open('/Users/zhouxiaoya/learngit/readme.txt','r')
print(fg_a)

dic ={fg_a:sheet_a,fg_b:sheet_b,fg_c:sheet_c}
filename_list = [fg_a,fg_b,fg_c]
for filename in filename_list:
	sheet_file = dic[filename]
	print(dic[filename])
	if(filename,sheet_file) in dic.items() :
	   i = 0
	   for line in filename:
	       line =line.strip()#去除字符串的首尾字符 
	       m = line.split(",")#以逗号分隔做成列表
	       i=i+1
	       j=0
	       for k in m:
	       	   sheet_file.write(i,j,k)
	       	   j=j+1
workbook.save('test.xls')

for filename in filename_list:
	filename.close()