from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # Images using relative paths
        img = Image.open(r"images\student.jpg").resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=150)

        img1 = Image.open(r"images\student1.jpg").resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=150)

        img2 = Image.open(r"images\student2.jpg").resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=150)

        img3 = Image.open(r"images\backgroundimg.jpg").resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1500, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"images\leftframe1.jpg").resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        # Course Information Frame
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=115)

        Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), width=17, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "Management", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"), width=17, state="readonly")
        course_combo["values"] = ("Select Course", "CSE", "IT", "BCA", "BBA", "MBA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), width=17, state="readonly")
        year_combo["values"] = ("Select Year", "First Year", "Second Year", "Third Year", "Fourth Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, sticky=W)
        sem_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=17, state="readonly")
        sem_combo["values"] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5", "Sem-6", "Sem-7", "Sem-8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student Information Frame
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold")).grid(row=0, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Class Division:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), width=18, state="readonly")
        div_combo["values"] = ("A", "B", "C", "D")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white").grid(row=1, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold")).grid(row=1, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white").grid(row=2, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold")).grid(row=2, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold")).grid(row=3, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white").grid(row=3, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold")).grid(row=3, column=3, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 13, "bold")).grid(row=4, column=1, padx=10, pady=5, sticky=W)

        Label(class_student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white").grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ttk.Entry(class_student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold")).grid(row=4, column=3, padx=10, pady=5, sticky=W)

        ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes").grid(row=5, column=0, pady=5)
        ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No").grid(row=5, column=1, pady=5)
        self.var_radio1.set("No")

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=195, width=710, height=35)

        Button(btn_frame, width=17, text="Save", command=self.add_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, width=17, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, width=17, text="Delete", command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, width=17, text="Reset", command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=3, y=235, width=710, height=35)

        Button(btn_frame1, width=35, text="Take Photo Sample", command=self.generate_dataset, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame1, width=35, text="Update Photo Sample", command=self.generate_dataset, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"images\rightframe2.jpg").resize((720, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(right_frame, image=self.photoimg_right).place(x=5, y=0, width=720, height=130)

        # Search Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.var_search_combo = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_combo, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll", "Phone", "Student_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search_txt = StringVar()
        ttk.Entry(search_frame, textvariable=self.var_search_txt, width=15, font=("times new roman", 13, "bold")).grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Button(search_frame, width=14, text="Search", command=self.search_data, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=3, padx=4)
        Button(search_frame, width=14, text="Show All", command=self.fetch_data, font=("times new roman", 12, "bold"), bg="blue", fg="white").grid(row=0, column=4, padx=4)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("Dep", "Course", "Year", "Sem", "Id", "Name", "Div", "Roll", "Gender", "Dob", "Email", "Phone", "Address", "Teacher", "Photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Id", text="Student Id")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Roll", text="Roll No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Dob", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="Photo Sample")

        self.student_table["show"] = "headings"
        for col in self.student_table["columns"]:
            self.student_table.column(col, width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root1234",
            database="face_recognizer"
        )

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            return
        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student Details added successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.close()
        except Exception as es:
            print("Fetch Error:", es)

    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content.get("values")
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])

    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
            return
        try:
            if messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root):
                conn = self.get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
            return
        try:
            if messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root):
                conn = self.get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM student WHERE Student_id=%s", (self.var_std_id.get(),))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success", "Successfully deleted student details", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("No")

    def search_data(self):
        if self.var_search_combo.get() == "Select" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Select search criteria and enter value", parent=self.root)
            return
        try:
            conn = self.get_connection()
            my_cursor = conn.cursor()
            query = f"SELECT * FROM student WHERE {self.var_search_combo.get()} LIKE %s"
            my_cursor.execute(query, (f"%{self.var_search_txt.get()}%",))
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            else:
                messagebox.showinfo("Result", "No matching records found", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
            return

        try:
            student_id = self.var_std_id.get()

            # Ensure data folder exists
            if not os.path.exists("data"):
                os.makedirs("data")

            # Check if student exists; if not, insert first
            conn = self.get_connection()
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE Student_id = %s", (student_id,))
            exists = my_cursor.fetchone()

            if not exists:
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    student_id, self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                    self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                    self.var_address.get(), self.var_teacher.get(), "Yes"
                ))
            else:
                my_cursor.execute("UPDATE student SET PhotoSample='Yes' WHERE Student_id=%s", (student_id,))

            conn.commit()
            self.fetch_data()
            conn.close()

            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    break
                gray = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    img_id += 1
                    face = cv2.resize(gray[y:y + h, x:x + w], (450, 450))
                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Capturing Samples - Press Enter to Finish Early", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            self.var_radio1.set("Yes")
            messagebox.showinfo("Result", f"100 Samples generated for Student ID: {student_id}", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()