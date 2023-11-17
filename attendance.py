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
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # ===============variables=================
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_status=StringVar()

        # first image
        img = Image.open(r"images\st4.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # img = Image.open(r"C:\Users\Vista\Desktop\images\student2.jpg")

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=45, width=800, height=200)

        # second image
        img1 = Image.open(r"images\st4.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=45, width=800, height=200)

         # background image
        img3 = Image.open(r"images\bg1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM",
                          font=("times new roman", 25, "bold"), bg="white", fg="navyblue")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=20, width=1300, height=450)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 15, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=430)

        # img_left = Image.open(r"images\view.jpg")
        # img_left = img_left.resize((700, 130), Image.ANTIALIAS)
        # self.photoimg_left = ImageTk.PhotoImage(img_left)

        # f_lbl = Label(Left_frame, image=self.photoimg_left)
        # f_lbl.place(x=5, y=0, width=690, height=130)

        left_inside_frame = Frame(Left_frame,relief=RIDGE,bd=2,bg="white")
        left_inside_frame.place(x=8, y=10, width=680, height=270)

        # label and entry

        # attendance id

        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 12, "bold"),
                                state="active")
        attendanceId_label.grid(row=0, column=0, padx=10,pady=15, sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_id,
                                    font=("times new roman", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10,pady=15, sticky=W)

        # name 
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"),
                                state="active")
        Name_label.grid(row=0, column=2, padx=10,pady=15, sticky=W)
        Name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_name,
                                    font=("times new roman", 12, "bold"))
        Name_entry.grid(row=0, column=3, padx=10,pady=15, sticky=W)

        # department
        Department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"),
                                state="active")
        Department_label.grid(row=1, column=0, padx=10,pady=15, sticky=W)
        Department_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_dep,
                                    font=("times new roman", 12, "bold"))
        Department_entry.grid(row=1, column=1, padx=10,pady=15, sticky=W)

        # time
        Time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"),
                                state="active")
        Time_label.grid(row=1, column=2, padx=10,pady=15, sticky=W)
        Time_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_time,
                                    font=("times new roman", 12, "bold"))
        Time_entry.grid(row=1, column=3, padx=10,pady=15, sticky=W)

        # date
        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"),
                                state="active")
        Date_label.grid(row=2, column=0, padx=10,pady=15, sticky=W)
        Date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_attend_date,
                                    font=("times new roman", 12, "bold"))
        Date_entry.grid(row=2, column=1, padx=10,pady=15, sticky=W)

        # attend status combo
        student_attend_label = Label(left_inside_frame,text="Attend-status:",font=("times new roman",12,"bold"))
        student_attend_label.grid(row=3,column=0,padx=10,pady=15,sticky=W)

        self.attend_status=ttk.Combobox(left_inside_frame,width=13,textvariable=self.var_attend_status,font=("times new roman",12,"bold"),state="readonly")
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=3,column=1,padx=10,pady=15,sticky=W)

       # buttons frame
        # btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        # btn_frame.place(x=2, y=350, width=680, height=50)

        save_btn = Button(Left_frame, text="Import csv",command=self.importCsv, width=13,
                          font=("times new roman", 8, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0,padx=10,pady=5)
        save_btn.place(x=10, y=300, width=100, height=30)

        update_btn = Button(Left_frame, text="Export csv",command=self.exportCsv, width=13, font=("times new roman", 8, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1)
        update_btn.place(x=120, y=300, width=100, height=30)

        # delete_btn = Button(Left_frame, text="Update", width=13, font=("times new roman", 8, "bold"), bg="blue",
        #                     fg="white")
        # delete_btn.grid(row=0, column=2)
        # delete_btn.place(x=230, y=300, width=100, height=30)

        reset_btn = Button(Left_frame, text="Reset",command=self.reset_data, width=13, font=("times new roman", 8, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=2)
        reset_btn.place(x=230, y=300, width=100, height=30)

        # right frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                 font=("times new roman", 15, "bold"))
        Right_frame.place(x=720, y=10, width=550, height=430)

        tabe_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        tabe_frame.place(x=10, y=5, width=520, height=335)

        # ==========scoll bar table==============
        scroll_x=ttk.Scrollbar(tabe_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabe_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(tabe_frame,column=("id","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        # ==================fetch data====================
    def fetch_data(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetch_data(mydata)

    # export scv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
            
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0])
        self.var_attend_name.set(rows[1])
        self.var_attend_dep.set(rows[2])
        self.var_attend_time.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_status.set(rows[5])

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_status.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()