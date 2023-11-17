from tkinter import *
from tkinter import ttk, messagebox
from turtle import update
import urllib.request
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set",
                          font=("times new roman", 30, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        img_top = Image.open(r"images\train2.png")
        img_top = img_top.resize((1400, 700), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1400, height=700)

        b1_1 = Button(self.root, text="TRAIN DATA",command=self.tarin_classifier, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      bg="gray", fg="white")
        b1_1.place(x=400, y=150, width=550, height=60)

    def tarin_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ==================Train the classifier and save===================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root) 
    root.mainloop()