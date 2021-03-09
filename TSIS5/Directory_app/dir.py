from tkinter import *
from tkinter.simpledialog import askstring
from tkinter import messagebox
import os
import shutil

root = Tk()
root.title("Explorer")
root.geometry("720x480+0+0")

absolute_path=os.getcwd().split('\\')

dirs=IntVar(root)
files=IntVar(root)

def display_files(): #Displays files in ListBox
    global dirs,files
    dirs.set(0)
    files.set(0)
    path='\\'.join(absolute_path)
    for i in os.listdir():
        if(os.path.isfile(path+'\{}'.format(i))):
            files.set(files.get()+1)
        else:
            dirs.set(dirs.get()+1)
        cwd.insert(END,i)

def change_dir(): #Changes Directory Forw And Backw
    os.chdir('\\'.join(absolute_path))
    cwd.delete(0,END)
    display_files()
    

def change_entry_back(event):
    cursel.set(cwd.get(cwd.curselection()))
    opt_menu.place_forget()
    seltext=''
    if(seltext!=cwd.get(cwd.curselection())):
        path_entry.delete(0,END)
    seltext=cwd.get(cwd.curselection())
    path_entry.insert(0,os.path.join(os.getcwd(),seltext))

def change_entry_forward(event):
    cursel_double.set(cwd.get(cwd.curselection()))
    try: 
        index=cwd.curselection()
        absolute_path.append(cwd.get(index))
        change_dir()
    except:
        try:
            text.delete('1.0',END)
            with open(cwd.get(cwd.curselection()),'rt',encoding='utf8') as rf:
                data=rf.read()
                text.insert(1.0,data)
            refresh_back()
        except:
            refresh_back()
        
            
def refresh_back(): #for Back Button
    absolute_path.pop()
    change_dir()

def delete(): #delets files and dirs
    if os.path.isdir(path_entry.get()):
        shutil.rmtree(path_entry.get())
    else:
        os.remove(path_entry.get())
    change_dir()

def menu_small_place(event): #right-mouse click menu
    opt_menu.place(x=event.x,y=event.y,bordermode=INSIDE,width=100)
    opt_menu.tkraise()

def menu_small(*args): #selection from right-mouse menu
    variable = askstring('Name','')
    try:
        if (opt_var.get()=="Rename"):
            os.rename(cwd.get(cwd.curselection()),variable)
        elif(opt_var.get()=="Create a file"):
            open(variable,'x').close()
        elif(opt_var.get()=="Create a directory"):
            os.mkdir(variable)
    except:
        messagebox.showinfo('Oops','Already exists.Choose another name,please',icon='warning')
    change_dir()

def save_file():
    with open(cursel_double.get(),'wt',encoding='utf8') as wf:
        wf.write(text.get('1.0',END))

#Buttons
back_bt = Button(text='Back', command=refresh_back, padx="14", pady="7", font="10")
back_bt.place(relx=0.001,rely=0.05,anchor='w',height=50,width=90,bordermode=OUTSIDE)
del_bt= Button(text='Del', command=delete, height=1, width=2, padx="14", pady="7", font="10")
del_bt.place(x=645,y=0)
save_bt = Button(text='Save', command=save_file, height=1, width=2, padx="14", pady="7", font="10")
save_bt.place(x=645,y=70)

#Option Menu
opt_var=StringVar(root)
opt_var.set("Choose...")
opt_menu=OptionMenu(root,opt_var,'Rename','Create a file','Create a directory')
opt_menu.config(width=90)
opt_var.trace('w',menu_small)

#Entry
path_entry=Entry(width=90)
path_entry.place(x=80,y=330)

#Scrollbar
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
#List Box
cwd=Listbox(yscrollcommand=scrollbar.set,height=20,width=30)
cwd.place(x=80,y=0)
display_files()
cwd.bind('<<ListboxSelect>>', change_entry_back)
cwd.bind('<Double-Button-1>', change_entry_forward)
cwd.bind('<Button-3>',menu_small_place)
cursel=StringVar()
cursel_double=StringVar()

#Text
text=Text(root,height=14,width=32,font='Arial 14',wrap=WORD)
text.delete('1.0',END)
text.place(x=270,y=2)

#Label
num_files=Label(textvariable=files,text=str(files.get()))
num_files.place(x=0,y=460)
dir_files=Label(textvariable=dirs,text=str(dirs.get()))
dir_files.place(x=40,y=460)
text1=Label(text="files,")
text1.place(anchor='sw',x=10,y=481)
text2=Label(text="directories:")
text2.place(anchor='sw',x=50,y=481)


root.mainloop()