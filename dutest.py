#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import xlwt
import sys
from xlrd import open_workbook
from xlutils.copy import copy

def main():
	
	data = xlrd.open_workbook('baitest.xls')
	#f = xlwt.Workbook()
	#sheet2 = f.add_sheet(u'baidu_app1')
	#lineinfo = "2201020"+"\t"+"wwt"+"\t"+"98076"
	#sheet2.write(0,0,lineinfo)
	#sheet2.write(2,4,'888111')
	#f.save('baitest.xls')
def addmain():
	xls_path = 'baitest.xls'
	xlsfile = open_workbook(xls_path) 
	wxlsfile = copy(xlsfile)
	sheet = wxlsfile.get_sheet(3)
	sheet.write(0,0,'20180406')
	wxlsfile.save(xls_path)
if __name__ == "__main__":
	addmain()
