from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Top Images
        img = Image.open(r"images\attendance3.jpg").resize((800, 200))
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=800, height=200)

        img1 = Image.open(r"images\attendance4.jpg").resize((800, 200))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open(r"images\backgroundimg.jpg").resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1500, height=600)

        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"images\leftframe1.jpg").resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=370)

        # Labels & Entry fields
        Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 11 bold").grid(row=0, column=2, padx=4, pady=8)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_roll, font="comicsansns 11 bold").grid(row=0, column=3, pady=8)

        Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold").grid(row=1, column=0)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_name, font="comicsansns 11 bold").grid(row=1, column=1, pady=8)

        Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold").grid(row=1, column=2)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_dep, font="comicsansns 11 bold").grid(row=1, column=3, pady=8)

        Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold").grid(row=2, column=0)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_time, font="comicsansns 11 bold").grid(row=2, column=1, pady=8)

        Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold").grid(row=2, column=2)
        ttk.Entry(left_inside_frame, width=22, textvariable=self.var_atten_date, font="comicsansns 11 bold").grid(row=2, column=3, pady=8)

        Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold").grid(row=3, column=0)
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=3, y=300, width=710, height=35)

        Button(btn_frame, width=17, text="Import csv", command=self.importCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, width=17, text="Export csv", command=self.exportCsv, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, width=17, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, width=17, text="Reset", command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right label frame (Table)
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=540)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            column=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
            self.AttendanceReportTable.column(col, width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        # AUTOMATICALLY LOAD ATTENDANCE ON WINDOW OPEN
        self.auto_load_attendance()

    def auto_load_attendance(self):
        global mydata
        mydata.clear()
        csv_file = "shorya.csv"
        if os.path.exists(csv_file):
            with open(csv_file, "r") as f:
                reader = csv.reader(f)
                rows = list(reader)
                # Skip header row if present
                if len(rows) > 0 and rows[0][0].lower() in ["id", "attendance id"]:
                    mydata = rows[1:]
                else:
                    mydata = rows
                self.fetchData(mydata)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        if fln:
            with open(fln, "r") as myfile:
                csvread = csv.reader(myfile)
                rows = list(csvread)
                if len(rows) > 0 and rows[0][0].lower() in ["id", "attendance id"]:
                    mydata = rows[1:]
                else:
                    mydata = rows
                self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found To Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile)
                    exp_write.writerow(["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance"])
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export", f"Data Exported to {os.path.basename(fln)} successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if rows:
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def update_data(self):
        if self.var_atten_id.get() == "":
            messagebox.showerror("Error", "Select record to update", parent=self.root)
            return

        global mydata
        updated_entry = [
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        ]

        # Update in memory
        for idx, row in enumerate(mydata):
            if row[0] == updated_entry[0] and row[5] == updated_entry[5]:
                mydata[idx] = updated_entry
                break

        # Save back to CSV
        with open("shorya.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "roll", "name", "department", "time", "date", "attendance"])
            writer.writerows(mydata)

        self.fetchData(mydata)
        messagebox.showinfo("Success", "Attendance record updated successfully!", parent=self.root)

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()