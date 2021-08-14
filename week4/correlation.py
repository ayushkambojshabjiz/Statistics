#Project: Correlation GUI
#Author: Ayush
#intern ID: 190016
#batch: CSE-SD
#date: 13-08-2021
#version: 1.0

from tkinter import *
import statistics
import xlrd
import openpyxl
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#some settings for xlrd to work fine
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

#printing mean, median, mode, SD in console for check working
value_mean=[2,5,6,9]
meanfinal=statistics.mean(value_mean)
print("result of mean:",meanfinal)

value_median=[1,2,3,8,9]
median_final=statistics.median(value_median)
print("result of median:",median_final)

value_mode=[2,5,3,2,8,3,9,4,2,5,6]
mode_final=statistics.mode(value_mode)
print("result of mode:",mode_final)

value_sd=[1,1.5,2,2.5,3,3.5,4,4.5,5]
sd_final=statistics.stdev(value_sd)
print("result of sd:",sd_final)


#bowser() function for function button.
def browse():
       #test location for xlsx file
       loc=(r"D:\python\file.xlsx")

#open workbook
       wb = xlrd.open_workbook(loc)       

#if we want to use sheet. 
#worksheet = wb.sheet_by_name("sheet")
       
#for showing all file
       worksheet = wb.sheet_by_index(0)

       i=1

       while(i<5):
           sn=worksheet.cell(i,0)
           rn=worksheet.cell(i,1)
           

#printing values in console
           
#print("",str(sn.value),"",str(rn.value),"",str(mrks.value))
           print("",int(sn.value),"",int(rn.value))
           i=i+1


  
# window title and size
root = Tk() 
root.title("GUI APP - Correlation in Python")
root.minsize(500, 600) 


#label
lab_1 = Label(root, text = 'Select the data file .xls/.xlsx', font =('Arial', 14))
lab_1.pack(side = "top", pady = 10) 

#textbox
#text_box = Text(
    
#    height=12,
#    width=40
#)
#text_box.pack(expand=True)
#text_box.place(x=90, y=60)
#text_box.config(state='disabled')




columns = ('#1', '#2')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('#1', text='x values')
tree.heading('#2', text='y values')


contacts = []
    #contacts.append((f'first {n}', f'last {n}'))

# adding data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)

def item_selected(event):
    for selected_item in tree.selection():
        # dictionary
        item = tree.item(selected_item)
        # list
        record = item['values']
        #
        showinfo(title='Information',
                message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

#tree.grid(row=0, column=0, sticky='nsew')
tree.place(x=190, y=350)
tree.pack()







#buttons
browse_btn = tk.Button(root, text = 'Browse', command=browse, height = 1, width = 7)
browse_btn.pack(side = RIGHT )
browse_btn.place(x=350, y=300)

result = Label(root, text = 'Result is: ', font =('Arial', 14), fg='blue')
result.pack(side = "top", pady = 10)
result.place(x=210, y=350)

result_fianl = Label(root, text = 'null', font =('Arial', 14), fg='blue')
result_fianl.pack(side = "top", pady = 10)
result_fianl.place(x=300, y=350)

#set result_fianl text if user press mean button
def mean():
       
        result_fianl.config(text=meanfinal)

        
#set result_fianl text if user press median button
def median():
       
        result_fianl.config(text=median_final)
        
#set result_fianl text if user press mode button
def mode():
       
        result_fianl.config(text=mode_final)

#set result_fianl text if user press sd button
def sd():
       
        result_fianl.config(text=sd_final)


#buttons placing

#mean btn and calling mean() function
mean_btn = tk.Button(root, text = 'Karl Peorson', command=mean, height = 1, width = 13)
mean_btn.pack(side = RIGHT )
mean_btn.place(x=100, y=410)

#median btn and calling median() function
median_btn = tk.Button(root, text = 'Rank correlation', command=median, height = 1, width = 13)
median_btn.pack(side = RIGHT )
median_btn.place(x=100, y=460)

#median btn and calling mode() function
mode_btn = tk.Button(root, text = 'Graph', command=mode, height = 1, width = 13)
mode_btn.pack(side = RIGHT )
mode_btn.place(x=320, y=410)

#sd btn and calling sd() function

#sd_btn = tk.Button(root, text = 'SD', command=sd, height = 1, width = 13)
#sd_btn.pack(side = RIGHT )
#sd_btn.place(x=350, y=460)

#quit btn and calling root.destroy
quitbtn = Button(root, text = 'Quit',command=root.destroy, fg='red', height = 1, width = 13)
quitbtn.pack(side = BOTTOM)
quitbtn.place(x=320, y=460)
#quitbtn.place(x=230, y=550)


        
mainloop()



  

        
