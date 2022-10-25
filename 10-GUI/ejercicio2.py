import tkinter 
import os,sys


ventana=tkinter.Tk()
ventana.title('Elige tu idima')
ventana.geometry('350x150')

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(0,weight=3)

def restart():
  os.execl(sys.executable, sys.executable, * sys.argv) 


lb=tkinter.Label(ventana,text='Idioma(s) a estudiar')
lb.grid(column=0,row=0,sticky=tkinter.W)

selected=tkinter.StringVar()
r1=tkinter.Radiobutton(ventana,text='Inglés',value=1,variable=selected)
r1.grid(column=0,row=1,sticky=tkinter.W)


selecionado=tkinter.StringVar()
r4=tkinter.Radiobutton(ventana,text='Aleman',value=2,variable=selecionado)
r4.grid(column=0,row=4,sticky=tkinter.W)
r2=tkinter.Radiobutton(ventana,text='Español',value=2,variable=selecionado)
r2.grid(column=0,row=2,sticky=tkinter.W)


r3=tkinter.Radiobutton(ventana,text='Portugues',value=1,variable=selecionado)
r3.grid(column=0,row=3,sticky=tkinter.W)

bReset=tkinter.Button(ventana,text='Resetar', width=10, command=restart)
bReset.grid(column=0,row=5,sticky=tkinter.W)

ventana.mainloop()

