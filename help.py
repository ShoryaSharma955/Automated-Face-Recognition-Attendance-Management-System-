from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"images\help1.jpg")
        img_top=img_top.resize((1530,720))
        self.photoimg_top=ImageTk.PhotoImage(img_top) 

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_label,text="Email: shoryash05@gmail.com",font=("times new roman",25,"bold"),bg="red")
        dev_label.place(x=915,y=355)






if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
