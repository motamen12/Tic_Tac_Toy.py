from tkinter import *
from tkinter import ttk
root=Tk()
# Grid
style=ttk.Style()
style.theme_use('classic')
ttk.Label(root,background='Green', text='Green').grid(row=0,column=0, sticky='snew')
ttk.Label(root,background='yellow', text='yellow').grid(row=0,column=1,  sticky='snew')
ttk.Label(root,background='blue', text='blue').grid(row=1,column=0, columnspan=2, sticky='snew')
ttk.Label(root,background='orange', text='orange').grid(row=0, column=2, rowspan=2, sticky='snew')
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
"""
# events
def key_press(event):
    print('type{}'.format(event.type))
    print('ctrol+c')
root.bind('<Control-c>',key_press)

def button_press(event):
    print('button is pressed')
bu=ttk.Button(root,text="click")
bu.pack()
bu.bind('<ButtonPress>',button_press)

# callback
bu=ttk.Button(root,text='click')
bu.pack()
bu1=ttk.Button(root,text='click 1')
bu1.pack()
bu2=ttk.Button(root,text='click 2')
bu2.pack()
def bu_clik(x):
    print('clicked:ْ{}'.format(x))
bu.config(command=lambda : bu_clik(0))
bu1.config(command=lambda : bu_clik(1))
bu2.config(command=lambda : bu_clik(2))

#entary
entry1=ttk.Entry(root,width=40)
entry1.pack()
bu1=ttk.Button(root,text='get text')
bu1.pack()
def bu_clik():
    print(entry1.get())
    entry1.delete(0,END)
bu1.config(command=bu_clik)
# text
T = Text(root, bg, fg, bd, height, width, font, ..)
"""
root.mainloop()
