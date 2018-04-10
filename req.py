#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#新建excle文件并写入数据
import xlwt
import xlutils.copy

#对xls文件初始化
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
#style_compression:表示是否压缩

#创建sheet对象,cell_overwrite_ok:表示是否可以覆盖单元格
sheet = workbook.add_sheet('test',cell_overwrite_ok=True)

sheet.write(0,0,'EnglishName') #0-行，0-列，EnglishName为写入内容
sheet.write(1,0,'Marcovaldo')
'''
txt1 = '中文名字'
sheet.write(0,1,txt1.decode('utf-8')) #此处需要将中文字符串解码成uniclde码

txt2 = '马可瓦多'
sheet.write(1, 1, txt2.decode('utf-8'))
'''
workbook.save(r'/Users/zhouxiaoya/learngit/Python/test1.xls')