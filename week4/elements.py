import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
root.geometry('550x600')

#city started
tk.Label(root, 
         text="City:",
#         height = 3, width = 10,
#         background = 'yellow', foreground ="black",
         
         justify = tk.LEFT,
         padx = 20).pack()

# Combobox
n = tk.StringVar() 
country = ttk.Combobox(root, width = 27, textvariable = n) 
  
# Adding list 
country['values'] = (' Ambala',  
                          ' Karnal', 
                          ' Chandigarh', 
                          ' Rohtak', 
                          ' Panipat', 
                          ' Kaithal', 
                          ' Kurukshetra', 
                          ' etc..') 
  
country.pack() 
country.current()



#state started
v = tk.IntVar()
v.set(1)

tk.Label(root, 
         text="Choose a state:",
         height = 4, width = 13,
                 
         ).pack()
languages = [("Haryana", 1),
   	     ("Punjab", 2),
    	     ("Uttar pardesh", 3),
             ("Gujrat", 4)]


for language, val in languages:
    tk.Radiobutton(root, 
                   text=language,
                   padx = 20, 
                   variable=v,                    
                   value=val).pack(anchor=tk.W)



lbl = Label(root, text = "Days", height = 0, width = 0)  
  
listbox = Listbox(root, fg = "yellow", bg="green")  
  
listbox.insert(1,"Monday")  
  
listbox.insert(2, "Tuesday")  
  
listbox.insert(3, "Wednesday")  

listbox.insert(4, "Thursday") 

listbox.insert(5, "Friday") 

listbox.insert(6, "Saturday") 

listbox.insert(7, "Sunday") 
  

lbl.pack()  
listbox.pack()  

tk.Label(root, 
         text="select number:",
         height = 3, width = 10,
         justify = tk.LEFT,
         padx = 20).pack(side = LEFT)

  
one = Checkbutton(root, text = "one", height = 2, width = 10)  
  
two = Checkbutton(root, text = "two", height = 2, width = 10)  
  
three = Checkbutton(root, text = "three", height = 2, width = 10)  
  
one.pack(side = LEFT)  
  
two.pack(side = LEFT)  
  
three.pack(side = LEFT)  

root.mainloop()
