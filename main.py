from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
from student import student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        # Top Header Images (using local relative paths)
        img = Image.open(r"images\college.jpg").resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=150)

        img1 = Image.open(r"images\face.png").resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=150)

        img2 = Image.open(r"images\college2.jpg").resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=150)

        # Background
        img3 = Image.open(r"images\backgroundimg.jpg").resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Live Clock
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=45)
        time()

        # Grid of Buttons
        # 1. Student Details
        img4 = Image.open(r"images\studentbutton4.png").resize((220, 220))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2").place(x=200, y=100, height=220, width=220)
        Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=200, y=300, height=40, width=220)

        # 2. Face Detector
        img5 = Image.open(r"images\facedetector.png").resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data).place(x=500, y=100, height=220, width=220)
        Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=500, y=300, height=40, width=220)

        # 3. Attendance
        img6 = Image.open(r"images\attendance.jpg").resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data).place(x=800, y=100, height=220, width=220)
        Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=800, y=300, height=40, width=220)

        # 4. Help Desk
        img7 = Image.open(r"images\helpdesk.png").resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.help_desk).place(x=1100, y=100, height=220, width=220)
        Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_desk, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=1100, y=300, height=40, width=220)

        # 5. Train Data
        img8 = Image.open(r"images\training.jpg").resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)
        Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data).place(x=200, y=380, height=220, width=220)
        Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=200, y=580, height=40, width=220)

        # 6. Photos
        img9 = Image.open(r"images\photo.jpg").resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)
        Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_image).place(x=500, y=380, height=220, width=220)
        Button(bg_img, text="Photos", cursor="hand2", command=self.open_image, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=500, y=580, height=40, width=220)

        # 7. Developer
        img10 = Image.open(r"images\developer.jpg").resize((220, 220))
        self.photoimg10 = ImageTk.PhotoImage(img10)
        Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.developer_data).place(x=800, y=380, height=220, width=220)
        Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=800, y=580, height=40, width=220)

        # 8. Exit
        img11 = Image.open(r"images\exit.png").resize((220, 220))
        self.photoimg11 = ImageTk.PhotoImage(img11)
        Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit).place(x=1100, y=380, height=220, width=220)
        Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="red", fg="white").place(x=1100, y=580, height=40, width=220)

    def open_image(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        os.startfile("data")

    def iExit(self):
        result = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if result:
            self.root.destroy()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_desk(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()