from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import cv2.face
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"images\training.jpg").resize((1530, 325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=1530, height=325)

        # Train button
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom = Image.open(r"images\training.jpg").resize((1530, 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "No 'data' directory found. Take photo samples first!", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]
        if len(path) == 0:
            messagebox.showerror("Error", "No image samples found in data folder!", parent=self.root)
            return

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert to grayscale
            image_np = np.array(img, 'uint8')
            # Extract id from: data/user.1.10.jpg
            file_name = os.path.split(image)[1]
            try:
                user_id = int(file_name.split('.')[1])
                faces.append(image_np)
                ids.append(user_id)
                cv2.imshow("Training Progress", image_np)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Skipping file {file_name}: {e}")

        ids = np.array(ids)

        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()