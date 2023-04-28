from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root=Tk()
root.title("Times")
root.title("600x600")
newsize=(100,100)
clock=ImageTk.PhotoImage(Image.open("a.jpg"))
c2=ImageTk.PhotoImage(Image.open("u.jpg"))
c=ImageTk.PhotoImage(Image.open("japan.jpg"))
c4=ImageTk.PhotoImage(Image.open("india.jpg"))
i=Label(root,text="India")
i.place(relx=0.2,rely=0.5,anchor=CENTER)
ic=Label(root,width=50,height=50)
ic['image']=c4
ic.place(relx=0.2,rely=0.35,anchor=CENTER)
it=Label(root)
it.place(relx=0.2,rely=0.65,anchor=CENTER)

a=Label(root,text="America")
a.place(relx=0.7,rely=0.5,anchor=CENTER)
ac=Label(root,width=50,height=50)
ac['image']=c2
ac.place(relx=0.7,rely=0.35,anchor=CENTER)
at=Label(root)
at.place(relx=0.7,rely=0.65,anchor=CENTER)

j=Label(root,text="Japan")
j.place(relx=0.5,rely=0.5,anchor=CENTER)
jc=Label(root,width=50,height=50)
jc['image']=c
jc.place(relx=0.5,rely=0.35,anchor=CENTER)
jt=Label(root)
jt.place(relx=0.5,rely=0.65,anchor=CENTER)

au=Label(root,text="Australia")
au.place(relx=0.9,rely=0.5,anchor=CENTER)
auc=Label(root,width=50,height=50)
auc['image']=c
auc.place(relx=0.9,rely=0.35,anchor=CENTER)
aut=Label(root)
aut.place(relx=0.9,rely=0.65,anchor=CENTER)
class India():
    def times (self):
        home=pytz.timezone("Asia/Kolkata")
        lt=datetime.now(home)
        ct=lt.strftime("%H:%M:%S")
        it["text"]="Time: "+ ct
        it.after(200,self.times)
class America():
    def times(self):
        home=pytz.timezone("US/Central")
        lt=datetime.now(home)
        ct=lt.strftime("%H:%M:%S")
        at["text"]="Time: "+ ct
        at.after(200,self.times)
class J():
    def times(self):
        home=pytz.timezone("Japan")
        lt=datetime.now(home)
        ct=lt.strftime("%H:%M:%S")
        jt["text"]="Time: "+ ct
        jt.after(200,self.times)
class AUS():
    def times(self):
        home=pytz.timezone("Australia/ACT")
        lt=datetime.now(home)
        ct=lt.strftime("%H:%M:%S")
        jt["text"]="Time: "+ ct
        jt.after(200,self.times)
oi=India()
oa=America()
oaus=AUS()
oj=J()
ib=Button(root,text="Show Time",command=oi.times)
ib.place(relx=0.2,rely=0.8,anchor=CENTER)
ab=Button(root,text="Show Time",command=oa.times)
ab.place(relx=0.7,rely=0.8,anchor=CENTER)
jb=Button(root,text="Show Time",command=oj.times)
jb.place(relx=0.5,rely=0.8,anchor=CENTER)
aub=Button(root,text="Show Time",command=oaus.times)
aub.place(relx=0.9,rely=0.8,anchor=CENTER)
root.mainloop()