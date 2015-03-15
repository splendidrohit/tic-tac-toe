from tkMessageBox import *
from sys import *

def check(n,r,c,tic):
    t1=t2=t3=t4=0
    for i in range(1,3):
        if(tic[(r+i)%3][c]==n):
            t1+=1
        if(tic[r][(c+i)%3]==n):
            t2+=1
        if((r==0 and c==0) or (r==1 and c==1) or (r==2 and c==2)):
            if(tic[(r+i)%3][(c+i)%3]==n):
                t3+=1
        if((r==0 and c==2) or (r==1 and c==1) or (r==2 and c==0)):
            if(tic[(r+i)%3][(c+2*i)%3]==n):
                t4+=1
    if(t1==2 or t2==2 or t3==2 or t4==2):
        return 1
    return 0


def checker(n,l,tac,tic):
    f=0
    for i in range(3):
        for j in range(3):
            if(tac[i][j]=='*'):
                tac[i][j]=n
                u=check(n,i,j,tac)
                if(n==0 and u==1):
                    tac[i][j]='*'
                    return 20
                if(n==1 and u==1):
                    tac[i][j]='*'
                    if(l==1):
			tac[i][j]=1
                        tic[i][j].config(text='X',font=('times',25,'bold'))
                        showinfo("oops","you loose")
                        exit(0)
                    return 0
                k=checker((n+1)%2,l+1,tac,tic)
                tac[i][j]='*'
                if(f==0):
                    r=i
                    c=j
                    p=k
                    f=1
                elif(n==1):
                    if(p>k):
                        p=k
                        r=i
                        c=j
                elif(n==0):
                    if(p<k):
                        p=k
                        r=i
                        c=j
    if(l==1 and f==1):
	tac[r][c]=1
        tic[r][c].config(text='X',font=('times',25,'bold'))
    if(l==1 and f==0):
        showinfo("oops..","match tie")
	exit(0)
    if(f==0):
        return 1
    return p+1

