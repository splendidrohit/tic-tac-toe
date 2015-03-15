from Tkinter import *
from tic import *
root=Tk()
top=None

def call(i,j):
	global tic,tac
	if(tac[i][j]=='*'):
		tac[i][j]=0
		tic[i][j].config(text='0',font=('times',25,'bold'))
		checker(1,1,tac,tic)
	else:
		showerror("sorry","already occupied")
	
def makewid(tic,i):	
	f=Frame(top)
	f.pack(expand=YES,fill=BOTH)
	l1=Label(f,bg='black')
	l1.pack(side=LEFT,expand=YES,fill=BOTH)
	l2=Label(f,bg='black')
	l2.pack(side=LEFT,expand=YES,fill=BOTH)
	l3=Label(f,bg='black')
	l3.pack(side=RIGHT,expand=YES,fill=BOTH)
	b1=Button(l1,bg='aquamarine',text=' ',command=(lambda:call(i,0)))
	b2=Button(l2,bg='aquamarine',text=' ',command=(lambda:call(i,1)))
	b3=Button(l3,bg='aquamarine',command=(lambda:call(i,2)))
	b1.pack(side=LEFT,expand=YES,fill=BOTH)
	b2.pack(side=RIGHT,expand=YES,fill=BOTH)
	b3.pack(side=LEFT,expand=YES,fill=BOTH)
	temp=[]
	temp.append(b1)
	temp.append(b2)
	temp.append(b3)
	tic.append(temp)
	del temp
tic=[]
tac=[]
def make():
	global top
	top=Toplevel()
	top.grab_set()
	Label(top,text="your mark is 0\ncomputer's mark is X",bg='red',font=('times',20,'italic')).pack(expand=YES,fill=BOTH)
	top.title("tic-tac-toe")
	top.resizable(0,0)
	top.minsize(500,500)
	for i in range(3):
		temp=['*','*','*']
		tac.append(temp)
		del temp
	for i in range(3):
		makewid(tic,i)
Label(root,text="HELLO EVERYONE\nWelcome to TIC-TAC-TOE\nDeveloped by\n ROHIT BHARDWAJ",bg='aquamarine',font=('time',20,'italic')).pack()
f=Frame(root,bg='red')
f.pack(expand=YES,fill=BOTH)
Button(f,text='play now',bg='black',fg='white',command=make).pack()
root.title("tic-tac-toe")
root.mainloop()
