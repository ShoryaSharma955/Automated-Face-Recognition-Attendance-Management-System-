from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import mysql.connector
from datetime import datetime
import os
import time


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Liveness Verified")

        title_lbl = Label(
            self.root,
            text="FACE RECOGNITION (ANTI-SPOOF LIVENESS)",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="red"
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"images\facedetector1.png").resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"images\facedetector2.png").resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_label_right = Label(self.root, image=self.photoimg_bottom)
        f_label_right.place(x=650, y=55, width=950, height=700)

        # Start Button
        b1_1 = Button(
            f_label_right,
            text="START RECOGNITION",
            cursor="hand2",
            command=self.face_recog,
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="white"
        )
        b1_1.place(x=330, y=630, height=40, width=300)

    # ======= Attendance Logger ==============================
    def mark_attendance(self, i, r, n, d):
        csv_file = "shorya.csv"

        if not os.path.exists(csv_file):
            with open(csv_file, "w", newline="") as f:
                f.write("id,roll,name,department,time,date,attendance\n")

        now = datetime.now()
        date_today = now.strftime("%d/%m/%Y")
        time_now = now.strftime("%H:%M:%S")

        with open(csv_file, "a", newline="") as f:
            f.write(f"{i},{r},{n},{d},{time_now},{date_today},Present\n")

    # ======= Face Recognition with 3-Minute Cooldown ==============================
    def face_recog(self):
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier not found! Train dataset first.", parent=self.root)
            return

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        eye_cascade_path = os.path.join(cv2.data.haarcascades, "haarcascade_eye.xml")
        eyeCascade = cv2.CascadeClassifier(eye_cascade_path)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        # 3 Minutes = 180 Seconds Cooldown
        COOLDOWN_PERIOD = 180  

        liveness_state = {}       # Tracks blink stages
        last_logged_time = {}     # Tracks last timestamp per student ID

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=8)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id_val, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                n, r, d, i = "Unknown", "Unknown", "Unknown", str(id_val)

                if confidence > 75:
                    try:
                        conn = mysql.connector.connect(
                            host="localhost",
                            user="root",
                            password="root1234",
                            database="face_recognizer"
                        )
                        my_cursor = conn.cursor()
                        my_cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id = %s", (str(id_val),))
                        row = my_cursor.fetchone()
                        if row:
                            n = str(row[0]).strip()
                            r = str(row[1]).strip()
                            d = str(row[2]).strip()
                            i = str(row[3]).strip()
                        conn.close()
                    except Exception as e:
                        print("DB Error:", e)

                if n != "Unknown":
                    current_timestamp = time.time()
                    time_since_last_scan = current_timestamp - last_logged_time.get(i, 0)
                    is_on_cooldown = time_since_last_scan < COOLDOWN_PERIOD

                    # Detect eyes for liveness verification
                    face_roi_gray = gray_image[y:y + int(h * 0.65), x:x + w]
                    eyes = eyeCascade.detectMultiScale(face_roi_gray, scaleFactor=1.15, minNeighbors=6, minSize=(25, 25))

                    if i not in liveness_state:
                        liveness_state[i] = {"stage": 0, "frames_closed": 0, "verified": False}

                    student_state = liveness_state[i]

                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 255, 0), 1)

                    num_eyes = len(eyes)

                    # Blink State Machine (Only active if not on cooldown)
                    if not is_on_cooldown and not student_state["verified"]:
                        if num_eyes >= 2 and student_state["stage"] == 0:
                            student_state["stage"] = 1

                        elif num_eyes < 2 and student_state["stage"] == 1:
                            student_state["frames_closed"] += 1
                            if student_state["frames_closed"] >= 1:
                                student_state["stage"] = 2

                        elif num_eyes >= 2 and student_state["stage"] == 2:
                            student_state["verified"] = True
                            student_state["stage"] = 3

                    # Display Student Info
                    cv2.putText(img, f"ID: {i} | Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r} | Dep: {d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

                    if is_on_cooldown:
                        # 3-minute cooldown is active
                        seconds_left = int(COOLDOWN_PERIOD - time_since_last_scan)
                        cv2.putText(img, f"ALREADY MARKED ({seconds_left}s left)", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.65, (0, 255, 255), 2)
                        cv2.putText(img, "Cooldown Active (No Repeat)", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 255), 2)

                    elif student_state["verified"]:
                        # Liveness verified & outside 3-minute cooldown: log attendance
                        cv2.putText(img, "REAL (Blink Verified)", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                        self.mark_attendance(i, r, n, d)
                        last_logged_time[i] = current_timestamp

                        # Reset state for next cycle after 3 minutes
                        student_state["verified"] = False
                        student_state["stage"] = 0
                        student_state["frames_closed"] = 0

                        cv2.putText(img, "ATTENDANCE RECORDED!", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)

                    else:
                        # Waiting for blink
                        cv2.putText(img, "PLEASE BLINK EYES...", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 165, 255), 2)
                        cv2.putText(img, "[Anti-Spoof Protected]", (x, y + h + 25), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 165, 255), 2)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

            # Top notification bar
            cv2.rectangle(img, (0, 0), (640, 35), (30, 30, 30), -1)
            cv2.putText(img, "Anti-Spoof Active | 3-Min Cooldown | Enter: Exit", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

            cv2.imshow("Welcome To Face Recognition - Press Enter to Exit", img)

            if cv2.waitKey(1) == 13:  # Enter key to close
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()