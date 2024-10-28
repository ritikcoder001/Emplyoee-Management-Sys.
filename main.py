from customtkinter import *
from PIL import Image
from tkinter import messagebox
def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "All fields are required")
    elif usernameEntry.get() == "ritikchauhan" and passwordEntry.get() == "1234321":
        messagebox.showinfo("Success", "Login is successful")
    else:
        messagebox.showerror("Error", "Wrong credentials")



    
root=CTk()
root.title('login page')


headinglabel=CTkLabel(root,text="Employee management System")
headinglabel.place(x=20,y=100)

usernameEntry=CTkEntry(root,placeholder_text="please enter username",width=180)
usernameEntry.place(x=50,y=150)
passwordEntry=CTkEntry(root,placeholder_text="plsease enter password",width=180,show="*")
passwordEntry.place(x=50,y=200)

loginButton=CTkButton(root,text="login",cursor="hand2",command=login)
loginButton.place(x=70,y=250)

root.mainloop()