from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Face Recognition Attendance System")
        self.root.geometry("1530x790+0+0")

        # ======= Background Image =======
        try:
            self.bg = ImageTk.PhotoImage(file=r"images\backgroundimg.jpg")
            lbl_bg = Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            self.root.config(bg="#1c2833")

        # ======= Main Login Frame =======
        frame = Frame(self.root, bg="white", bd=2, relief=RIDGE)
        frame.place(x=540, y=140, width=450, height=520)

        title = Label(
            frame,
            text="Get Started",
            font=("times new roman", 28, "bold"),
            fg="#2c3e50",
            bg="white"
        )
        title.place(x=40, y=30)

        subtitle = Label(
            frame,
            text="Login with your credentials",
            font=("times new roman", 13),
            fg="gray",
            bg="white"
        )
        subtitle.place(x=40, y=80)

        # ======= Form Fields =======
        # Email
        lbl_email = Label(
            frame,
            text="Email Address",
            font=("times new roman", 14, "bold"),
            fg="#34495e",
            bg="white"
        )
        lbl_email.place(x=40, y=130)

        self.txt_email = ttk.Entry(frame, font=("times new roman", 13))
        self.txt_email.place(x=40, y=165, width=370, height=35)

        # Password
        lbl_pass = Label(
            frame,
            text="Password",
            font=("times new roman", 14, "bold"),
            fg="#34495e",
            bg="white"
        )
        lbl_pass.place(x=40, y=220)

        self.txt_pass = ttk.Entry(frame, font=("times new roman", 13), show="*")
        self.txt_pass.place(x=40, y=255, width=370, height=35)

        # ======= Buttons =======
        btn_login = Button(
            frame,
            command=self.login,
            text="Login",
            font=("times new roman", 15, "bold"),
            bd=0,
            cursor="hand2",
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            activeforeground="white"
        )
        btn_login.place(x=40, y=320, width=370, height=45)

        btn_register = Button(
            frame,
            command=self.register_window,
            text="New User? Register Here",
            font=("times new roman", 12),
            bg="white",
            fg="#2980b9",
            bd=0,
            cursor="hand2"
        )
        btn_register.place(x=40, y=390)

        btn_forgot = Button(
            frame,
            command=self.forgot_password_window,
            text="Forgot Password?",
            font=("times new roman", 12),
            bg="white",
            fg="#e67e22",
            bd=0,
            cursor="hand2"
        )
        btn_forgot.place(x=40, y=430)

    # ======= Database Connector Helper =======
    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root1234",
            database="face_recognizer"
        )

    # ======= Login Action =======
    def login(self):
        email = self.txt_email.get().strip()
        pwd = self.txt_pass.get().strip()

        if email == "" or pwd == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (email, pwd))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password!", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome, {row[0]} {row[1]}!", parent=self.root)
                # Destroy login and launch Main Attendance System
                self.root.destroy()
                main_root = Tk()
                Face_Recognition_System(main_root)
                main_root.mainloop()

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Database Error: {str(es)}", parent=self.root)

    # ======= Register Subwindow =======
    def register_window(self):
        self.reg_window = Toplevel(self.root)
        self.reg_window.title("Register New User")
        self.reg_window.geometry("800x620+380+80")
        self.reg_window.config(bg="white")
        self.reg_window.grab_set()

        title = Label(
            self.reg_window,
            text="REGISTER HERE",
            font=("times new roman", 24, "bold"),
            bg="white",
            fg="#27ae60"
        )
        title.place(x=50, y=20)

        # Fields
        Label(self.reg_window, text="First Name", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=80)
        self.txt_fname = ttk.Entry(self.reg_window, font=("times new roman", 12))
        self.txt_fname.place(x=50, y=110, width=320, height=32)

        Label(self.reg_window, text="Last Name", font=("times new roman", 12, "bold"), bg="white").place(x=420, y=80)
        self.txt_lname = ttk.Entry(self.reg_window, font=("times new roman", 12))
        self.txt_lname.place(x=420, y=110, width=320, height=32)

        Label(self.reg_window, text="Contact No.", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=160)
        self.txt_contact = ttk.Entry(self.reg_window, font=("times new roman", 12))
        self.txt_contact.place(x=50, y=190, width=320, height=32)

        Label(self.reg_window, text="Email Address", font=("times new roman", 12, "bold"), bg="white").place(x=420, y=160)
        self.txt_reg_email = ttk.Entry(self.reg_window, font=("times new roman", 12))
        self.txt_reg_email.place(x=420, y=190, width=320, height=32)

        Label(self.reg_window, text="Security Question", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=240)
        self.combo_sec_q = ttk.Combobox(self.reg_window, font=("times new roman", 11), state="readonly")
        self.combo_sec_q["values"] = (
            "Select",
            "Your First Pet Name?",
            "Your Birth City?",
            "Your Favorite Teacher?"
        )
        self.combo_sec_q.current(0)
        self.combo_sec_q.place(x=50, y=270, width=320, height=32)

        Label(self.reg_window, text="Security Answer", font=("times new roman", 12, "bold"), bg="white").place(x=420, y=240)
        self.txt_sec_a = ttk.Entry(self.reg_window, font=("times new roman", 12))
        self.txt_sec_a.place(x=420, y=270, width=320, height=32)

        Label(self.reg_window, text="Password", font=("times new roman", 12, "bold"), bg="white").place(x=50, y=320)
        self.txt_reg_pass = ttk.Entry(self.reg_window, font=("times new roman", 12), show="*")
        self.txt_reg_pass.place(x=50, y=350, width=320, height=32)

        Label(self.reg_window, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white").place(x=420, y=320)
        self.txt_cpass = ttk.Entry(self.reg_window, font=("times new roman", 12), show="*")
        self.txt_cpass.place(x=420, y=350, width=320, height=32)

        # Checkbox
        self.var_check = IntVar()
        chk = Checkbutton(
            self.reg_window,
            variable=self.var_check,
            text="I Agree to the Terms & Conditions",
            font=("times new roman", 11),
            onvalue=1,
            offvalue=0,
            bg="white"
        )
        chk.place(x=50, y=410)

        # Submit Button
        btn_reg = Button(
            self.reg_window,
            command=self.register_data,
            text="REGISTER NOW",
            font=("times new roman", 14, "bold"),
            bg="#27ae60",
            fg="white",
            cursor="hand2",
            bd=0
        )
        btn_reg.place(x=250, y=470, width=280, height=45)

    def register_data(self):
        if (
            self.txt_fname.get() == ""
            or self.txt_contact.get() == ""
            or self.txt_reg_email.get() == ""
            or self.combo_sec_q.get() == "Select"
            or self.txt_sec_a.get() == ""
            or self.txt_reg_pass.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required!", parent=self.reg_window)
            return

        if self.txt_reg_pass.get() != self.txt_cpass.get():
            messagebox.showerror("Error", "Password & Confirm Password do not match!", parent=self.reg_window)
            return

        if self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms & conditions!", parent=self.reg_window)
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.txt_reg_email.get(),))
            row = my_cursor.fetchone()

            if row is not None:
                messagebox.showerror("Error", "User with this email already exists!", parent=self.reg_window)
            else:
                my_cursor.execute(
                    "INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_reg_email.get(),
                        self.combo_sec_q.get(),
                        self.txt_sec_a.get(),
                        self.txt_reg_pass.get()
                    )
                )
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully! You can now login.", parent=self.reg_window)
                self.reg_window.destroy()

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.reg_window)

    # ======= Forgot Password Subwindow =======
    def forgot_password_window(self):
        if self.txt_email.get().strip() == "":
            messagebox.showerror("Error", "Please enter your Email in the login field first!", parent=self.root)
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT securityQ, securityA FROM register WHERE email=%s", (self.txt_email.get().strip(),))
            row = my_cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "No account registered with this email!", parent=self.root)
                return

            saved_q, self.saved_a = row[0], row[1]

            self.fpass_window = Toplevel(self.root)
            self.fpass_window.title("Reset Password")
            self.fpass_window.geometry("450x380+540+200")
            self.fpass_window.config(bg="white")
            self.fpass_window.grab_set()

            Label(self.fpass_window, text="RESET PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="#e67e22").place(x=40, y=20)

            Label(self.fpass_window, text=f"Security Question:\n{saved_q}", font=("times new roman", 12), bg="white", justify=LEFT).place(x=40, y=70)

            Label(self.fpass_window, text="Security Answer", font=("times new roman", 12, "bold"), bg="white").place(x=40, y=130)
            self.txt_ans = ttk.Entry(self.fpass_window, font=("times new roman", 12))
            self.txt_ans.place(x=40, y=155, width=360, height=30)

            Label(self.fpass_window, text="New Password", font=("times new roman", 12, "bold"), bg="white").place(x=40, y=200)
            self.txt_new_pass = ttk.Entry(self.fpass_window, font=("times new roman", 12), show="*")
            self.txt_new_pass.place(x=40, y=225, width=360, height=30)

            btn_reset = Button(
                self.fpass_window,
                command=self.reset_password,
                text="Update Password",
                font=("times new roman", 13, "bold"),
                bg="#27ae60",
                fg="white",
                bd=0,
                cursor="hand2"
            )
            btn_reset.place(x=120, y=290, width=200, height=40)

        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)

    def reset_password(self):
        if self.txt_ans.get().strip() == "" or self.txt_new_pass.get().strip() == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.fpass_window)
            return

        if self.txt_ans.get().strip().lower() != self.saved_a.strip().lower():
            messagebox.showerror("Error", "Incorrect security answer!", parent=self.fpass_window)
            return

        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE register SET password=%s WHERE email=%s", (self.txt_new_pass.get().strip(), self.txt_email.get().strip()))
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Password updated successfully! Please login.", parent=self.fpass_window)
            self.fpass_window.destroy()
        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.fpass_window)


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()