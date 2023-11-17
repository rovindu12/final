from email import message
from importlib.resources import contents
from tkinter import *
from tkinter import ttk, messagebox
from turtle import update
import urllib.request
from PIL import Image, ImageTk
import mysql.connector
from numpy import delete
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # ==============variables==================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_regNo = StringVar()
        self.var_name = StringVar()
        self.var_lecturer = StringVar()
        self.var_search= StringVar()
        self.var_searchTX= StringVar()

        img = Image.open(r"C:\Users\Vista\Desktop\images\Banners.png")
        img = img.resize((1400,120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=25, y=-10, width=1300, height=150)

        # background image
        img3 = Image.open(r"C:\Users\Vista\Desktop\images\uni1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 25, "bold"), bg="white", fg="brown")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20, y=50, width=1300, height=500)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=480)

        img_left = Image.open(r"images\st4.jpg")
        img_left = img_left.resize((685, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=685, height=130)

        # current course
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="current course information",
                                          font=("times new roman", 12, "bold"))
        current_course_frame.place(x=12, y=135, width=670, height=120)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"),
                          state="active")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=17)
        dep_combo["values"] = ("Select Department", "Computer Science", "Physical Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"),
                               state="active")
        semester_label.grid(row=1, column=0, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem,
                                      font=("times new roman", 12, "bold"), width=17)
        semester_combo["values"] = (
            "Select Semester", "Year 1 sem 1", "Year 1 sem 2", "Year 2 sem 1", "Year 2 sem 2", "Year 3 sem 1",
            "Year 3 sem 2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"),
                                  state="active")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_label_entry = ttk.Entry(current_course_frame, width=19, textvariable=self.var_course,
                                      font=("times new roman", 12, "bold"))
        course_label_entry.grid(row=0, column=3, padx=4, sticky=W)

        # Year
        Year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"),
                           state="active")
        Year_label.grid(row=1, column=2, padx=10, sticky=W)

        Year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=17)
        Year_combo["values"] = (
            "Select Year", "15/16", "16/17", "17/18", "18/19")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information frame
        class_Student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class Student information",
                                         font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=12, y=260, width=670, height=120)

        # student Reg No
        studentId_label = Label(class_Student_frame, text="Student ID", font=("times new roman", 12, "bold"),
                                state="active")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        studentId_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_regNo,
                                    font=("times new roman", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student Name
        studentName_label = Label(class_Student_frame, text="Student RegNo", font=("times new roman", 12, "bold"),
                                  state="active")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)
        studentName_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_name,
                                      font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Lecturer Name
        lecturerName_label = Label(class_Student_frame, text="Student Name", font=("times new roman", 12, "bold"),
                                   state="active")
        lecturerName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        lecturerName_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_lecturer,
                                       font=("times new roman", 12, "bold"))
        lecturerName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="take photo sample",
                                     value="Yes")
        radionbtn1.grid(row=4, column=0)

        
        radionbtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No photo sample",
                                     value="No")
        radionbtn1.grid(row=4, column=1)

        # buttons frame
        btn_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=12, y=385, width=670, height=50)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=10,
                          font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0,padx=8,pady=10)
        

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=10, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=1,padx=8,pady=10)
        

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=10, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        delete_btn.grid(row=0, column=2,padx=8,pady=10)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=10, font=("times new roman", 10, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3,padx=8,pady=10)

        take_photo_btn = Button(btn_frame,command=self.generate_dataset , text="Take Photo Sample", width=15, font=("times new roman", 10, "bold"),
                                bg="blue",
                                fg="white")
        take_photo_btn.grid(row=0, column=5, padx=10,pady=10)

        # =============================right label frame=============================
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=720, y=10, width=550, height=480)

        img_right = Image.open(r"images\length3.jpg")
        img_right = img_right.resize((535, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=535, height=130)

        # ================Search System=============

        Search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text="Search System",
                                  font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=540, height=80)

        search_label = Label(Search_frame,text="Search By:", font=("times new roman", 12, "bold"), bg="red",
                             fg="white",
                             state="active")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        self.var_searchTX=StringVar()
        search_combo = ttk.Combobox(Search_frame,textvariable=self.var_searchTX, font=("times new roman", 12, "bold"), width=17)
        search_combo["values"] = ("Select","student name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Search_frame,textvariable=self.var_search, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=4, pady=5, sticky=W)

        search_btn = Button(Search_frame,command=self.search_data, text="Search", width=10, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        # ===============Table Frame=============
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=220, width=540, height=220)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,
                                          column=("dep", "course", "year", "sem", "regNo", "name", "lecturer"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("regNo", text="ID")
        self.student_table.heading("name", text="Student RegNo")
        self.student_table.heading("lecturer", text="Student Name")
        self.student_table["show"] = "headings"

        # set column width
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("regNo", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("lecturer", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ==================FUNCTION DECLARATION=================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_regNo.get() == "":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_regNo.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_lecturer.get(),
                                                                                            self.var_radio1.get()
                                                                                            
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        # ====================fetch data==========================
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()    
            conn.close()

        # ====================get cursor============================= 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 

        self.var_dep.set(data[0]),
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_regNo.set(data[4])
        self.var_name.set(data[5])
        self.var_lecturer.set(data[6])
        self.var_radio1.set(data[7])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get() == "" or self.var_regNo.get() == "":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s ,Name=%s,Lecturer=%s,PhotoSample=%s where Student_id=%s",(

                                                                                            self.var_dep.get(),
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_sem.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_lecturer.get(),
                                                                                            self.var_radio1.get(),
                                                                                            self.var_regNo.get()
                                                                                            
                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


            # delete function
    def delete_data(self):
        if self.var_regNo.get() == "":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno ("Delete","Do you want to delete this student",parent=self.root)   
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer",port=3306)
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_regNo.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    # ===========================Search Data===================
    
    
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognizer',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT Dep,course,Year,Semester,Name,Lecturer,PhotoSample FROM student where Student_id='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Student_id= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

            # =============reset data==================

    def reset_data(self):
        self.var_dep.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_sem.set("")
        self.var_regNo.set("")
        self.var_name.set("")
        self.var_lecturer.set("")

# =========================generate data set or take photo samples=========================

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_regNo.get() == "":
                messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s ,Name=%s,Lecturer=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_lecturer.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_regNo.get()==id+1
                                                                                            
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                

                # ==============load predefined data on face frontals from opencv=================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+"."+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
               
                
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
