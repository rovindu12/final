from tkinter import *
from tkinter import ttk, messagebox
from turtle import update
import urllib.request
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # img=Image.open(r"images\back2.jpg")
        # img=img.resize((1366,130),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # # set image as lable
        # f_lb1 = Label(self.root,image=self.photoimg)
        # f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"images\back1.webp")
        bg1=bg1.resize((1400,600),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1400,height=600)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # title_lbl = Label(self.root, text="FACE RECOGNITION",
        #                   font=("times new roman", 30, "bold"), bg="white", fg="RED")
        # title_lbl.place(x=0, y=0, width=1400, height=45)

        # # left image
        # img_top = Image.open(r"images\face5.png")
        # img_top = img_top.resize((650, 700), Image.ANTIALIAS)
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        # f_lbl = Label(self.root, image=self.photoimg_top)
        # f_lbl.place(x=0, y=45, width=650, height=700)

        # # right image
        # img_right = Image.open(r"C:\Users\Vista\Desktop\images\two.jpg")
        # img_right = img_right.resize((700, 700), Image.ANTIALIAS)
        # self.photoimg_right = ImageTk.PhotoImage(img_right)

        # f_lbl = Label(self.root, image=self.photoimg_right)
        # f_lbl.place(x=650, y=45, width=700, height=700)

        # ====================button with image=====================
        # std_img_btn=Image.open(r"images\back.webp")
        # std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        # std_b1.place(x=600,y=170,width=180,height=180)

        # std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="navyblue")
        # std_b1_1.place(x=600,y=350,width=180,height=45)


        # button
        b1_1 = Button(bg_img, text="Detect Face And Mark Your Attendance", cursor="hand2",command=self.face_recog,
                      font=("times new roman", 17, "bold"),
                      bg="blue", fg="white")
        b1_1.place(x=480, y=550, width=450, height=50)

    # =========================attendance=====================
    def mark_attendance(self,n,i,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((n not in name_list) and (i not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{d},{dtString},{d1},Present")

    # ===========================face recognition=====================

    def face_recog(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Name from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence > 77:
                    cv2.putText(img,f"ID:{n}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,150,255),3)
                    cv2.putText(img,f"RegNO:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,150,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,150,255),3)
                    self.mark_attendance(n,i,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

                return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root) 
    root.mainloop()