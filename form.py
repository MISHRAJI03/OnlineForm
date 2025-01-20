# MODULES IMPORTING
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import tkinter.messagebox as message_box
import mysql.connector as sql_con

#TO CLEAR THE DETAILS ENTERED BY THE USER
def clear():
    txt_full_name.delete(0,"end")
    txt_parent_name.delete(0,"end")
    txt_parent_occupation.delete(0,"end")
    cmb_date.current(0)
    cmb_month.current(0)
    cmb_year.current(0)
    txt_permanent_address.delete(0,"end")
    txt_contact_number.delete(0,"end")
    txt_email_id.delete(0,"end")

#TO FETCH DATA PROVIDED BY THE USER
def register_data():
    fn = txt_full_name.get()
    pn = txt_parent_name.get()
    op = txt_parent_occupation.get()
    dt = cmb_date.get()
    mt = cmb_month.get()
    yr = cmb_year.get()
    ad = txt_permanent_address.get()
    no = txt_contact_number.get()
    em = txt_email_id.get()
    cb = check_box_var.get()
    if fn==""or pn==""or op==""or dt=="Date"or mt=="Month"or yr=="Year"or ad==""or no==""or em=="":
        message_box.showinfo("ERROR","ALL FIELDS ARE REQUIRED")
    elif cb=="off":
        message_box.showinfo("ERROR","PLEASE AGREE OUR TERMS AND CONDITIONS")
    else:
        con = sql_con.connect(host="localhost", user="root", password="MISHRAJI", database="admission")
        cur = con.cursor()
        cur.execute("insert into online_admission(Applicant_Name, Parent_Name, Parent_Occupation,"
                    "Date_of_Birth, Month_of_Birth, Year_of_Birth, Permanent_Address, Contact_Number, Email_ID)"
                    "values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fn,pn,op,dt,mt,yr,ad,no,em))
        con.commit()
        message_box.showinfo("NOTIFICATION","APPLIED SUCCESFULLY")
        clear()
        con.close()
        
#MAIN WINDOW
root = Tk()
root.title("Registration Window")
root.geometry("1280x786")

#BACKGROUND IMAGE
root.bg = ImageTk.PhotoImage(file="C:\CLASS 12\COMPUTER SCIENCE\BG image 3.jpeg")
bg = Label(root, image=root.bg, anchor=NW).place(x=0,y=0)
frame = Frame(root, bg="yellow")
frame.place(x=500, y=0, width=800, height=800)

#TEXTS
title = Label(frame,text="ADMISSION FORM", font=("Times New Roman", 35, "bold"),
              bg="yellow",fg="Green").place(x=120,y=60)
full_name = Label(frame,text="FULL NAME OF APPLICANT", font=("Times New Roman", 13, "bold"),
                  bg="yellow", fg="Black").place(x=50,y=170)
parent_name = Label(frame,text="PARENT NAME", font=("Times New Roman", 13, "bold"),
                    bg="yellow", fg="Black").place(x=50,y=220)
parent_occupation = Label(frame,text="PARENT OCCUPATION", font=("Times New Roman", 13, "bold"),
                          bg="yellow", fg="Black").place(x=50,y=270)
date_of_birth = Label(frame,text="DATE OF BIRTH (DD/MM/YYYY)", font=("Times New Roman", 13, "bold"),
                      bg="yellow", fg="Black").place(x=50,y=320)
permanent_address = Label(frame,text="PERMANENT ADDRESS", font=("Times New Roman", 13, "bold"),
                          bg="yellow", fg="Black").place(x=50,y=370)
contact_number = Label(frame,text="CONTACT NUMBER", font=("Times New Roman", 13, "bold"),
                       bg="yellow", fg="Black").place(x=50,y=420)
email_id = Label(frame,text="EMAIL ID", font=("Times New Roman", 13, "bold"),
                 bg="yellow", fg="Black").place(x=50,y=470)

#ENTRY BOXES
txt_full_name = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)
txt_parent_name = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)
txt_parent_occupation = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)
txt_permanent_address = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)
txt_contact_number = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)
txt_email_id = Entry(frame,font=("Times New Roman",13),bg="light grey",bd=0)

#POSITIONS
txt_full_name.place(x=340,y=170,width=290)
txt_parent_name.place(x=340,y=220,width=290)
txt_parent_occupation.place(x=340,y=270,width=290)
txt_permanent_address.place(x=340,y=370,width=290)
txt_contact_number.place(x=340,y=420,width=290)
txt_email_id.place(x=340,y=470,width=290)

#COMBO BOXES
cmb_date = ttk.Combobox(frame,font=("Times New Roman",13,"bold"),state="readonly",justify=CENTER)
cmb_date["values"] = ("Date","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18",
                      "19","20","21","22","23","24","25","26","27","28","29","30","31")
cmb_date.place(x=340,y=320,width=85)
cmb_date.current(0)
cmb_month = ttk.Combobox(frame,font=("Times New Roman",13,"bold"),state="readonly",justify=CENTER)
cmb_month["values"] = ("Month","January","February","March","April",
                       "May","June","July","August","September","October","November","December")
cmb_month.place(x=433,y=320,width=100)
cmb_month.current(0)
cmb_year = ttk.Combobox(frame,font=("Times New Roman",13,"bold"),state="readonly",justify=CENTER)
cmb_year["values"] = ("Year","1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001",
                      "2002","2003","2004","2004","2005","2006","2007","2008","2009","2010")
cmb_year.place(x=540,y=320,width=90)
cmb_year.current(0)

#CHECK BOX
check_box_var = StringVar()
check_box = Checkbutton(frame,text="I AGREE THE TERMS AND CONDITIONS", variable=check_box_var,
                        onvalue="on",offvalue="off",cursor="hand2",font=("Times New Roman",13,"bold"),
                        bg="yellow",fg="Black")
check_box.deselect()
check_box.place(x=165,y=520)

#BUTTON
registration_button = Button(frame,text="SUBMIT",font=("Times New Roman",15,"bold"), command=register_data)
registration_button.place(x=310,y=570)

root.mainloop()


