import xlrd
import openpyxl
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True


loc= (r"D:\python\file.xlsx")

wb= xlrd.open_workbook(loc)

worksheet = wb.sheet_by_index(0)

i=1
while(i<5):
	sn= worksheet.cell(i,0)
	mrks=worksheet.cell(i,1)
	print(" ",int(sn.value), " ",int(mrks.value))
	i=i+1
