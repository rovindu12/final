from tkinter import *
from tkinter import ttk
from typing import Any
import urllib.request
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognizor import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
    
     # first image
        img = Image.open(r"C:\Users\Vista\Desktop\images\Banners.png")
        img = img.resize((1500,160), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=25, y=-10, width=1300, height=180)

        # background image
        img3 = Image.open(r"images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1530, height=710)

        title_lbl = Label(bg_img, text="WELCOME  TO  FACE  RECOGNITION  ATTENDANCE  SYSTEM  (FAS)",
                          font=("times new roman", 15, "bold"), bg="white", fg="brown")
        title_lbl.place(x=0, y=10, width=1400, height=45)

        # STUDENT BUTTON
        img4 = Image.open(r"images\a1.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2",command=self.student_details)
        b1.place(x=250, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2",command=self.student_details,
                      font=("times new roman", 12, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=250, y=280, width=220, height=40)

        # FACE DETECTOR
        img5 = Image.open(r"images\face6.jpeg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,command=self.face_data, cursor="hand2")
        b1.place(x=550, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 12, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=550, y=280, width=220, height=40)

        # attendance face button
        img7 = Image.open(r"images\attend.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        b1.place(x=850, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman", 12, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=850, y=280, width=220, height=40)

        # Train face button
        img8 = Image.open(r"images\train6.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=250, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text="Train", cursor="hand2",command=self.train_data, font=("times new roman", 12, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=250, y=530, width=220, height=40)

        # Photos face button
        img6 = Image.open(r"images\train8.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.open_img)
        b1.place(x=550, y=330, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 12, "bold"),
                      bg="brown", fg="white")
        b1_1.place(x=550, y=530, width=220, height=40)

    def open_img(self):
        os.startfile("data")
    
    # ==================Functions Buttons==============

    def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)

    def train_data(self):
            self.new_window = Toplevel(self.root)
            self.app = Train(self.new_window)

    def face_data(self):
            self.new_window = Toplevel(self.root)
            self.app = Face_Recognition(self.new_window)
    
    def attendance_data(self):
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
