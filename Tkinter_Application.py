from tkinter import *
import random
import string
window=Tk()
window.title('wife')
window.geometry('350x350')  #SIZE OF WINDOW
label=Label(window,text='ENTER YOUR LUCKY NUMBER',font=('arial',(15)))
label.pack()
entry=Entry(window)
entry.pack()
entry.focus_set()  #TO GET THE INSERTION POINT TO THE BOX
label=Label(window,text='your name',font=('arial',(15)))
label.pack()
entry1=Entry(window)
entry1.pack()
def wife():
    root=Tk()   #TO CREATE A NEW WINDOW TO DISPALY THE RESULT
    root.title('result')
    root.geometry('750x350')
    global entry1 #MAKE ENTRY1 AS GLOBAL SO THAT YOU CAN ACCESS ANYWHERE
    name= entry1.get()
    b=list(string.ascii_uppercase)  #STRING.ASCII_UPPER CASE IS A FUNCTION SO THAT WE IMPORTED STRING LIBRARY
    a=random.choice(b)
    label=Label(root,text='your name is {} your wife name starts with the letter {}'.format(name,a),font=('arial',(15)))
    label.pack()


btn = Button(window, text="LETS FIND", command=wife) #CALLING 'WIFE' FUNCTION
btn.pack()
window.mainloop()