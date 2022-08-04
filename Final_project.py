#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkcalendar import Calendar, DateEntry
from tkinter import ttk, messagebox
from tktimepicker import AnalogPicker, AnalogThemes, constants
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import tkinter


class app1:



    
    def clear_all(self):
        for item in self.listBox.get_children():
            self.listBox.delete(item)
    
    def delete_module(self):
        txt_codes = self.txt_code.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if self.txt_code.get()!="" and self.txt_name.get()!="":
            try:
                sql = "select * from module where m_id = %s "
                mycursor.execute(sql,[(self.txt_code.get())]) 
                results = mycursor.fetchall()
                if len(results)==0:
                    messagebox.showerror("Error","Invalid course code")
                  
                sql = "select * from coursework where m_id = %s "
                mycursor.execute(sql,[(self.txt_code.get())]) 
                results = mycursor.fetchall()
                if results:
                    messagebox.showerror("Error","kindly remove course work or requirements and try again")
                    sql = "DELETE FROM `coursework` WHERE c_id=%s"
                    val = (self.txt_code.get(),)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                else:
                    sql = "DELETE FROM `module` WHERE m_id=%s"
                    val = (txt_codes,)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    lastid = mycursor.lastrowid
                    messagebox.showinfo("information", "Record Delete successfully...")
                    self.txt_code.delete(0, END)
                    self.txt_name.delete(0, END)
                    self.show()

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
    
    def show(self):
        self.clear_all()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="saad")
        mycursor = mysqldb.cursor()
        
        mycursor.execute("SELECT `m_id`, `m_name` FROM `module` ")
        records = mycursor.fetchall()
        
        
        for j, (module_ID,module_Name) in enumerate(records, start=1):
            self.listBox.insert("", "end", values=(module_ID,module_Name))
            mysqldb.close()   
    def GetValue(self,event):
        self.txt_code.delete(0, END)
        self.txt_name.delete(0, END)
        row_id = self.listBox.selection()[0]
        select = self.listBox.set(row_id)
        self.txt_code.insert(0,select['Module_ID'])
        self.txt_name.insert(0,select['Module_Name'])

        
    def update_module(self):
        txt_code = self.txt_code.get()
        txt_des =self.txt_name.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if self.txt_code.get()!="" and self.txt_name.get()!="":
            try:
                sql = "select * from module where m_id = %s "
                mycursor.execute(sql,[(self.txt_code.get())]) 
                results = mycursor.fetchall()
                if len(results)==0:
                    messagebox.showerror("Error","Invalid course code")
                           
                else:

                    sql = "UPDATE `module` SET `m_name`=%s WHERE m_id=%s "
                    val = (txt_des,txt_code)
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    lastid = mycursor.lastrowid
                    messagebox.showinfo("information", "Record Updated successfully...")
                    self.txt_code.delete(0, END)
                    self.txt_name.delete(0, END)
                    self.show()
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()  
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
            
            
    def __init__(self, root):
        self.root = root
        self.root.title("Module Screen")
        self.root.geometry("900x600")
        self.root.resizable(False,False)
        self.bg=PhotoImage(file="images/1.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,width=300,relheight=1)
        
        Frame_module=Frame(self.root,bg="white")
        Frame_module.place(x=302,y=0,height=600,width=1000)
        
        title=Label(Frame_module,text="Module Screen",font=("Bahnschrift",35,"bold"),fg="#d77337",bg="white").place(x=0,y=0)
        
        lbl_code=Label(Frame_module,text="Module code",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=60,y=110)
        self.txt_code=Entry(Frame_module,font=("Consolas",15),bg="lightgray")
        self.txt_code.place(x=50,y=150,width=200,height=35)
        
        
        lbl_name=Label(Frame_module,text="Module Name",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=50,y=210)
        self.txt_name=Entry(Frame_module,font=("Consolas",15),bg="lightgray")
        self.txt_name.place(x=50,y=250,width=200,height=80)
        

        cols = ('Module_ID', 'Module_Name')
        self.listBox = ttk.Treeview(Frame_module, columns=cols, show='headings' )
 
        
        self.listBox = ttk.Treeview(Frame_module, columns=cols, show='headings',height=9 )

        scrollbar = ttk.Scrollbar(Frame_module, orient='vertical', command=self.listBox.yview)
        scrollbar.grid(row=0, column=1) 
        scrollbar.place(x=515, y=150,height=210)

        self.listBox['yscrollcommand'] = scrollbar.set
        
        self.listBox.column("# 1",anchor=CENTER, stretch=NO, width=100)
        self.listBox.column("# 2",anchor=CENTER, stretch=NO, width=150)

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=1,rowspan=1)
            self.listBox.place(x=260, y=150)
        self.show()
        self.listBox.bind('<Double-Button-1>',self.GetValue)
        self.time = () 
         
            

        login_btn=Button(Frame_module,text="Create",width="10",command=self.insert_module,cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=85,y=540)
        login_btn2=Button(Frame_module,text="Edit",width="10",command=self.update_module,cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=230,y=540)
        login_btn3=Button(Frame_module,text="Delete",width="10",command=self.delete_module,cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=380,y=540)
        self.button4 = Button(root, text="course work",width="10",cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15), padx="1m", pady="1m")
        self.button4.pack()
        self.button4.place(x=380,y=350)
        self.button4.bind("<Button-1>", self.openwindow2)

        self.openprompt(root)
        
    def openprompt(self,root):
        
        root=Tk()
       
        window4 = app4(root)
        root.mainloop()
        
    def openwindow2(self, root):
        
        root=Tk()
        txt_code=self.txt_code.get()
 
        window2 = app2(root,txt_code)
        root.mainloop()
        
        
    def openwindow3(self, root):
        root=Tk()
        txt_code=self.txt_code2.get()
        window3 = app3(root,txt_code)
        root.mainloop()       

           
    def insert_module(self):
        mysqldb=mysql.connector.connect( host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if mysqldb.is_connected():
            if self.txt_code.get()!="" and self.txt_name.get()!="":
                sql = "select * from module where m_id = %s "
                mycursor.execute(sql,[(self.txt_code.get())]) 
                results = mycursor.fetchall()
                if results:
                    messagebox.showerror("Error"," Module code already exits")
                else:
                    sql = "INSERT INTO `module`(`m_id`, `m_name`) VALUES (%s,%s)"
                    val=(self.txt_code.get(),self.txt_name.get())
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    messagebox.showinfo("Module Screen","Record insert sucessfully")
                    self.show()
                    

            else:
                messagebox.showerror("Error"," kindly fill All fields")     

      
        else:
            print ("Error")

class app2(app1):

    
    def updateTime(self , time):
        self.txt_t.delete(0,END)
        z=time
        t_format=str(z[0])+":"+str(z[1])+" "+str(z[2])
        self.txt_t.insert(0,t_format)


    
    def get_time(self):
        top = Toplevel(root)
        top.title("Time")
        time_picker = AnalogPicker(top)
        time_picker.pack(expand=True, fill="both")
        theme = AnalogThemes(time_picker)
        theme.setPurple()
        ok_btn = Button(top, text="ok",command=lambda:self.updateTime(time_picker.time()))
        ok_btn.pack()
        
    def clear_all(self):
        for item in self.listBox.get_children():
            self.listBox.delete(item)
    
    def delete_coursework(self,m_code):
        txt_codes = self.txt_code2.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if self.txt_code2.get()!="" and self.txt_des.get()!="" and self.txt_date.get()!="" and self.txt_t.get()!="":

            try:
                sql = "select * from coursework where c_id = %s "
                mycursor.execute(sql,[(self.txt_code2.get())]) 
                results = mycursor.fetchall()
                if len(results)==0:
                    messagebox.showerror("Error"," user not found")
                else: 
                    sql = "DELETE FROM `requirement` WHERE c_id=%s"
                    val = (txt_codes,)
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    sql = "DELETE FROM `coursework` WHERE c_id=%s"
                    val = (txt_codes,)
                    mycursor.execute(sql, val)
                    mysqldb.commit()

                    lastid = mycursor.lastrowid
                    messagebox.showinfo("information", "Record Delete successfully...")
                    self.txt_code2.delete(0, END)
                    self.txt_des.delete(0, END)
                    self.txt_date.delete(0, END)
                    self.txt_t.delete(0, END)
                    self.show(m_code)

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
    
    def show(self,m_code):
        self.clear_all()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="saad")
        mycursor = mysqldb.cursor()
        sql = "SELECT `c_id`, `c_des`, DATE(due_date), `Time` FROM `coursework` where m_id = %s "
        mycursor.execute(sql,[(m_code)]) 
        records = mycursor.fetchall()
        
        for j, (course_ID, course_description, Due_Date, Time) in enumerate(records, start=1):
            self.listBox.insert("", "end", values=(course_ID, course_description, Due_Date, Time))
            mysqldb.close()   
    def GetValue(self,event):
        self.txt_code2.delete(0, END)
        self.txt_des.delete(0, END)
        self.txt_date.delete(0, END)
        self.txt_t.delete(0, END)
        row_id = self.listBox.selection()[0]
        select = self.listBox.set(row_id)
        self.txt_code2.insert(0,select['course_ID'])
        self.txt_des.insert(0,select['course_description'])
        self.txt_date.insert(0,select['Due_Date'])
        self.txt_t.insert(0,select['Time'])
        
    def update_coursework(self,m_code):
        txt_code = self.txt_code2.get()
        txt_des =self.txt_des.get()
        txt_date = self.txt_date.get()
        txt_t = self.txt_t.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if self.txt_code2.get()!="" and self.txt_des.get()!="" and self.txt_date.get()!="" and self.txt_t.get()!="":
            try:
                sql = "select * from coursework where c_id = %s "
                mycursor.execute(sql,[(self.txt_code2.get())]) 
                results = mycursor.fetchall()
                if len(results)==0:
                    messagebox.showerror("Error"," user not found")
                else:    
                    sql = "UPDATE `coursework` SET `c_des`=%s,`due_date`=%s,`Time`=%s WHERE c_id=%s"
                    val = (txt_des,txt_date,txt_t ,txt_code)
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    lastid = mycursor.lastrowid
                    messagebox.showinfo("information", "Record Updated successfully...")
                    self.show(m_code)
                    self.txt_code2.delete(0, END)
                    self.txt_des.delete(0, END)
                    self.txt_date.delete(0, END)
                    self.txt_t.delete(0, END)
                
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()  
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
            
            
    def __init__(self, root,m_code):
        
        self.root = root
        self.root.title("course Work")
        self.root.geometry("800x600")
        self.root.resizable(False,False)
        
        Frame_coursework=Frame(self.root,bg="white")
        Frame_coursework.place(x=0,y=0,height=600,width=900)
        
        title=Label(Frame_coursework,text="Course Work",font=("Bahnschrift",35,"bold"),fg="#d77337",bg="white").place(x=350,y=0)
        
        lbl_code=Label(Frame_coursework,text="Course code",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=60,y=110)
        self.txt_code2=Entry(Frame_coursework,font=("Consolas",15),bg="lightgray")
        self.txt_code2.place(x=50,y=150,width=200,height=35)
        
        
        lbl_des=Label(Frame_coursework,text="Description",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=50,y=210)
        self.txt_des=Entry(Frame_coursework,font=("Consolas",15),bg="lightgray")
        self.txt_des.place(x=50,y=250,width=200,height=80)
        
        
        lbl_duedate=Label(Frame_coursework,text="Due Date",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=50,y=340)
        self.txt_date=DateEntry(Frame_coursework,font=("Consolas",15),bg="lightgray",date_pattern='y-mm-dd')
        self.txt_date.place(x=50,y=380,width=200,height=40)
        
        
                
        lbl_t=Label(Frame_coursework,text="Time",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=50,y=440)
        self.txt_t=Entry(Frame_coursework,font=("Consolas",15),bg="lightgray")
        self.txt_t.place(x=50,y=480,width=200,height=40)
        

        time_btn=Button(Frame_coursework,text="Set Time",width="10",command=self.get_time,cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=250,y=480)

        cols = ('course_ID', 'course_description','Due_Date','Time')
        self.listBox = ttk.Treeview(Frame_coursework, columns=cols, show='headings' )
 
        
        self.listBox = ttk.Treeview(Frame_coursework, columns=cols, show='headings',height=9 )

        scrollbar = ttk.Scrollbar(Frame_coursework, orient='vertical', command=self.listBox.yview)
        scrollbar.grid(row=0, column=1) 
        scrollbar.place(x=714, y=150,height=226)

        self.listBox['yscrollcommand'] = scrollbar.set
        
        self.listBox.column("# 1",anchor=CENTER, stretch=NO, width=100)
        self.listBox.column("# 2",anchor=CENTER, stretch=NO, width=150)
        self.listBox.column("# 3",anchor=CENTER, stretch=NO, width=100)
        self.listBox.column("# 4",anchor=CENTER, stretch=NO, width=100)

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=1, column=1,rowspan=1)
            self.listBox.place(x=260, y=150)
        self.show(m_code)
        self.listBox.bind('<Double-Button-1>',self.GetValue)
        self.time = () 
        course_code= m_code
            

        create_btn=Button(Frame_coursework,text="Create",width="10",command=lambda: self.insert_coursework(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=85,y=540)
        update_btn2=Button(Frame_coursework,text="Edit",width="10",command=lambda: self.update_coursework(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=230,y=540)
        delete_btn3=Button(Frame_coursework,text="Delete",width="10",command=lambda: self.delete_coursework(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=380,y=540)
        self.button4 = Button(root, text="Requirements",width="15",cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15))
        self.button4.pack()
        self.button4.place(x=520,y=540)
        self.button4.bind("<Button-1>", self.openwindow3) 
    
    def insert_coursework(self,m_code):
    
        mysqldb=mysql.connector.connect( host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if mysqldb.is_connected():
            if self.txt_code2.get()!="" and self.txt_des.get()!="" and self.txt_date.get()!="" and self.txt_t.get()!="":
                sql = "select * from coursework where c_id = %s "
                mycursor.execute(sql,[(self.txt_code2.get())]) 
                results = mycursor.fetchall()
                if results:
                    messagebox.showerror("Error"," course code already exits")
                else:
                    sql = "INSERT INTO `coursework`(m_id,`c_id`, `c_des`, `due_date`, `Time`) VALUES (%s,%s,%s,%s,%s)"
                    val=(m_code,self.txt_code2.get(),self.txt_des.get(),self.txt_date.get(),self.txt_t.get())
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    messagebox.showinfo("Course work","Record insert sucessfully")
                    self.show(m_code)
                    

            else:
                messagebox.showerror("Error"," kindly fill All fields")     

      
        else:
            print ("Error")

            
class app3():

        
    def clear_all(self):
        for item in self.listBox.get_children():
            self.listBox.delete(item)
    
    def delete_requirement(self,m_code):

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if  self.txt_des.get()!="" :
            try:
                sql = "DELETE FROM `requirement` WHERE c_id=%s"
                val = (m_code,)
                mycursor.execute(sql, val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Delete successfully...")
                self.txt_des.delete(0, END)
                self.show(m_code)

            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
    
    def show(self,m_code):
        self.clear_all()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="saad")
        mycursor = mysqldb.cursor()
        sql = "SELECT `c_id`, `c_req`  FROM `requirement` where c_id = %s "
        mycursor.execute(sql,[(m_code)]) 
        records = mycursor.fetchall()
        
        
        for j, (course_ID, course_requirement,) in enumerate(records, start=1):
            self.listBox.insert("", "end", values=(course_ID, course_requirement))
            mysqldb.close()   
    def GetValue(self,event):
        self.txt_des.delete(0, END)
        row_id = self.listBox.selection()[0]
        select = self.listBox.set(row_id)
        self.txt_des.insert(0,select['course_Requirements'])

        
    def update_requirement(self,m_code):
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if self.txt_des.get()!="" :
            try:
                sql = "UPDATE `requirement` SET `c_req`=%s WHERE c_id=%s"
                val = (self.txt_des.get(),m_code,)
                mycursor.execute(sql,val)
                mysqldb.commit()
                lastid = mycursor.lastrowid
                messagebox.showinfo("information", "Record Updated successfully...")
                self.txt_des.delete(0, END)
                self.show(m_code)
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close()  
        else:
            messagebox.showerror("Error"," kindly fill All fields")  
            
            
    def __init__(self, root,m_code):
        
        self.root = root
        self.root.title("course Work")
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        
        Frame_requirement=Frame(self.root,bg="white")
        Frame_requirement.place(x=0,y=0,height=600,width=900)
        
        title=Label(Frame_requirement,text="Requirements",font=("Bahnschrift",35,"bold"),fg="#d77337",bg="white").place(x=150,y=0)
        

        
        
        lbl_des=Label(Frame_requirement,text="Description",font=("Bahnschrift",15,"bold"),fg="gray",bg="white").place(x=50,y=110)
        self.txt_des=Entry(Frame_requirement,font=("Consolas",15),bg="lightgray")
        self.txt_des.place(x=50,y=150,width=200,height=200)
        


        cols = ('course_ID', 'course_Requirements')
        self.listBox = ttk.Treeview(Frame_requirement, columns=cols, show='headings' )
 
        
        self.listBox = ttk.Treeview(Frame_requirement, columns=cols, show='headings',height=9 )

        scrollbar = ttk.Scrollbar(Frame_requirement, orient='vertical', command=self.listBox.yview)
        scrollbar.grid(row=0, column=1) 
        scrollbar.place(x=515, y=150,height=220)

        self.listBox['yscrollcommand'] = scrollbar.set
        
        self.listBox.column("# 1",anchor=CENTER, stretch=NO, width=100)
        self.listBox.column("# 2",anchor=CENTER, stretch=NO, width=150)
 

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=2, column=2,rowspan=2)
            self.listBox.place(x=260, y=150)
        self.show(m_code)
        self.listBox.bind('<Double-Button-1>',self.GetValue)
        self.time = () 
        course_code= m_code
            

        create_btn=Button(Frame_requirement,text="Create",width="10",command=lambda: self.insert_requirement(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=85,y=540)
        update_btn=Button(Frame_requirement,text="Edit",width="10",command=lambda:self.update_requirement(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=230,y=540)
        delete_btn=Button(Frame_requirement,text="Delete",width="10",command=lambda:self.delete_requirement(m_code),cursor="hand2",fg="white",bg="#d77337",font=("Consolas",15)).place(x=380,y=540)
        
        
    def insert_requirement(self,m_code):
        mysqldb=mysql.connector.connect( host="localhost",user="root",password="",database="saad")
        mycursor=mysqldb.cursor()
        if mysqldb.is_connected():
            if  self.txt_des.get()!="":
                sql = "select * from requirement where c_id = %s "
                mycursor.execute(sql,[(m_code)]) 
                results = mycursor.fetchall()
                if results:
                    messagebox.showerror("Error"," course code already exits")
                else:
                    sql = "INSERT INTO `requirement`(`c_id`, `c_req`) VALUES (%s,%s)"
                    val=(m_code,self.txt_des.get())
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    messagebox.showinfo("Course work","Record insert sucessfully")
                    self.show(m_code)
                    

            else:
                messagebox.showerror("Error"," kindly fill All fields")     

      
        else:
            print ("Error")
            
            
class app4():

        
    def clear_all(self):
        for item in self.listBox.get_children():
            self.listBox.delete(item)
    

    
    def show(self):
        self.clear_all()
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="saad")
        mycursor = mysqldb.cursor()
        sql = "SELECT m_id ,c_id,c_des,due_date FROM coursework WHERE due_date > NOW() AND due_date < CURDATE()+ INTERVAL 7 DAY"
        mycursor.execute(sql) 
        records = mycursor.fetchall()
        
        
        for j, (mid,cid,cd,date) in enumerate(records, start=1):
            self.listBox.insert("", "end", values=(mid,cid,cd,date))
            mysqldb.close()   


            
    def __init__(self, root):
        
        self.root = root
        self.root.title("up comming")
        self.root.geometry("700x600")
        self.root.resizable(False,False)
        
        Frame_requirement=Frame(self.root,bg="white")
        Frame_requirement.place(x=0,y=0,height=600,width=900)
        
        title=Label(Frame_requirement,text="Up coming Course Works",font=("Bahnschrift",35,"bold"),fg="#d77337",bg="white").place(x=100,y=0)
        


        cols = ('Module_ID', 'Course_code','Course_des','Date')
        self.listBox = ttk.Treeview(Frame_requirement, columns=cols, show='headings' )
 
        
        self.listBox = ttk.Treeview(Frame_requirement, columns=cols, show='headings',height=9 )

        scrollbar = ttk.Scrollbar(Frame_requirement, orient='vertical', command=self.listBox.yview)
        scrollbar.grid(row=0, column=1) 
        scrollbar.place(x=600, y=220,height=220)

        self.listBox['yscrollcommand'] = scrollbar.set
        
        self.listBox.column("# 1",anchor=CENTER, stretch=NO, width=100)
        self.listBox.column("# 2",anchor=CENTER, stretch=NO, width=150)
        self.listBox.column("# 3",anchor=CENTER, stretch=NO, width=150)
        self.listBox.column("# 4",anchor=CENTER, stretch=NO, width=150)
 

        for col in cols:
            self.listBox.heading(col, text=col)
            self.listBox.grid(row=2, column=2,rowspan=2)
            self.listBox.place(x=50, y=220)
        self.show()

            
            
            
            


root=Tk()
hope = app1(root)
root.mainloop()

