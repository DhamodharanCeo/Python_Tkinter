from tkinter import*               #IMPORT TKINTER

window = Tk()  #CREATES A BLANK WINDOW
window.title('LOGIN PAGE')
window.geometry('350x350')
label1=Label(window,text='USERNAME')
label1.grid(row=2,column=1)
label2=Label(window,text='PASSWORD')
label2.grid(row=4,column=1)
entry1=Entry(window)
entry1.grid(row=2,column=2)
entry2=Entry(window)
entry2.grid(row=4,column=2)
def success():
    root=Tk()
    root.title('SUCCESSFUL')
    label3=Label(root,text='SUCCESSFULLY LOGGED IN',font=('araial',(20)))
    label3.pack()
    root.mainloop()
btn=Button(window,text='SUBMIT',command=success)
btn.grid(columnspan=5)


window.mainloop()
