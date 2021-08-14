from tkinter import * 
from tkinter import messagebox
 
top = Tk()  
top.geometry("500x550")
top.title("GUI APP - Correlation in Python")

myText=StringVar()
wr = StringVar()



def upper():
	co= wr.get()
	myText.set(co.upper())

def lower():
	co= wr.get()
	myText.set(co.lower())

def toggle():
	co= wr.get()
	str=""
	for x in co:
		if(x.isupper()):
			str+= x.lower()
		if(x.islower()):
			str+=x.upper()		
	myText.set(str)

def sentence():
	co= wr.get()
	str=""
	i=0
	for x in co:
		i=i+1
		if(i==1):
			str+= x.upper()
		else:
			str+=x.lower()
	myText.set(str)


heading = Label(top, text = "Enter a word or sentence")

heading.place(x = 100,y = 40)

resultt = Label(top, text = "Result:")
resultt.place(x=180,y=200)


res = Label(top, text = "", fg="BLUE", textvariable=myText).place(x=230,y=200)

myText.set("")


word = Entry(top,textvariable = wr)
word.focus_set()
word.place(x=100, y=70,width=350)

button1 = Button(top, text = "Upper",command=upper).place(x = 100, y = 250,width=100)
button2 = Button(top, text = "Lower",command=lower).place(x = 300, y = 250,width=100)
button3 = Button(top, text = "TOGGLE", command= toggle).place(x = 100, y = 300,width=100)
button4 = Button(top, text = "Sentence", command=sentence).place(x = 300, y = 300,width=100)


quitBt= Button(top, text = "EXIT", command = top.destroy).place(x=200,y =370,width=80)

top.mainloop()
