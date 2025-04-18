# Module
from tkinter import *
import sqlite3

# App base
App = Tk()
App.geometry("520x780")
App.title("My Work Tracker")
heading = Label(text="My Work Tracker",bg="black",fg="white",font="150",width="500",height="3")
heading.pack()

# database
conn = sqlite3.connect("Work's_database.db")
C = conn.cursor()
C.execute("CREATE TABLE IF NOT EXISTS data (Execution_date text, Customer_name text, City text, Serial_number text, Date_of_submission_of_the_report  text, Sum_of_appraisals text, Profit_before_tax text, Start_of_the_day_KM text, End_of_the_day_KM text, KM_per_day text)")

# Submit data function
def submit():
    Promil = 0.00035
    #Insert info to the database
    conn = sqlite3.connect("Work's_database.db")
    C = conn.cursor()
    C.execute("INSERT INTO data VALUES (:Execution_date, :Customer_name, :Acity, :Serial_number, :Date_of_submission_of_the_report, :Sum_of_appraisals, :Profit_before_tax , :Start_of_the_day_KM, :End_of_the_day_KM, :KM_per_day)",
              {
                    'Execution_date': Execution_date.get(),
                    'Customer_name': Customer_name.get(),
                    'Acity': City.get(),
                    'Serial_number': Serial_number.get(),
                    'Date_of_submission_of_the_report': Date_of_submission_of_the_report.get(),
                    'Sum_of_appraisals': Sum_of_appraisals.get(),
                    'Profit_before_tax': Promil * float(Sum_of_appraisals.get()),
                    'Start_of_the_day_KM': Start_of_the_day_KM.get(),
                    'End_of_the_day_KM': End_of_the_day_KM.get(),
                    'KM_per_day': float(End_of_the_day_KM.get()) - float(Start_of_the_day_KM.get()),
              })
    
    #Clear input box
    Execution_date.delete(0, END)
    Customer_name.delete(0, END)
    City.delete(0, END)
    Serial_number.delete(0, END)
    Date_of_submission_of_the_report.delete(0, END)
    Sum_of_appraisals.delete(0, END)
    Start_of_the_day_KM.delete(0, END)
    End_of_the_day_KM.delete(0, END)

    conn.commit()
    conn.close()                
    
# Delete data function
def Delete_data():
    conn = sqlite3.connect("Work's_database.db")
    C = conn.cursor()
    C.execute("DELETE from data")
    conn.commit()
    conn.close()    

# Sum_profit function
Pick_a_month_profit = Entry(App, width="9")
Pick_a_month_profit.place(x=360, y=527)  
def Sum_profit() :
    conn = sqlite3.connect("Work's_database.db")
    C = conn.cursor()
    C.execute("SELECT SUM(Profit_before_tax) FROM data WHERE substr(Execution_date,4 ,2) = :The_month_she_choose",{'The_month_she_choose': Pick_a_month_profit.get()})
    Fetch_data_profit = C.fetchall()
    print_Fetch_data = "Sum of profit :" + str(Fetch_data_profit) + "\n"
    Summary_lable = Label(App, text=print_Fetch_data)
    Summary_lable.place(x=135, y=630)
    #Clear input box
    Pick_a_month_profit.delete(0, END)
    conn.commit()
    conn.close() 

# Sum appraisals function
Pick_a_month_appraisals = Entry(App, width="9")
Pick_a_month_appraisals.place(x=360, y=567)  
def Sum_appraisals():
    conn = sqlite3.connect("Work's_database.db")
    C = conn.cursor()
    C.execute("SELECT SUM(Sum_of_appraisals) FROM data WHERE substr(Execution_date, 4, 2) = :The_month_she_choose",{'The_month_she_choose': Pick_a_month_appraisals.get()})
    Fetch_data_appraisals = C.fetchall()
    print_Fetch_data = "Sum of appraisals :" + str(Fetch_data_appraisals) + "\n"
    Summary_lable = Label(App, text=print_Fetch_data)
    Summary_lable.place(x=135, y=650)
    #Clear input box
    Pick_a_month_appraisals.delete(0, END)
    conn.commit()
    conn.close() 

# Sum KM function
Pick_a_month_KM = Entry(App, width="9")
Pick_a_month_KM.place(x=360, y=607)  
def Sum_KM():
    conn = sqlite3.connect("Work's_database.db")
    C = conn.cursor()
    C.execute("SELECT SUM(KM_per_day) FROM data WHERE substr(Execution_date, 4, 2) = :The_month_she_choose",                              {'The_month_she_choose': Pick_a_month_KM.get()})
    Fetch_data_KM = C.fetchall()
    print_Fetch_data = "Sum of KM :" + str(Fetch_data_KM) + "\n"
    Summary_lable = Label(App, text=print_Fetch_data)
    Summary_lable.place(x=135, y=670)
    #Clear input box
    Pick_a_month_KM.delete(0, END)
    conn.commit()
    conn.close() 
    
# Text box function
Execution_date = Entry(App, width="34")
Customer_name = Entry(App, width="34")
City = Entry(App, width="34")
Serial_number = Entry(App, width="34")
Date_of_submission_of_the_report = Entry(App, width="34")
Sum_of_appraisals = Entry(App, width="34")
Start_of_the_day_KM = Entry(App, width="34")
End_of_the_day_KM = Entry(App, width="34")

# Text box Placement
Execution_date.place(x=135, y=85)
Customer_name.place(x=135,y=130)
City.place(x=135, y=175)
Serial_number.place(x=135, y=220)
Date_of_submission_of_the_report.place(x=135, y=265)
Sum_of_appraisals.place(x=135, y=310)
Start_of_the_day_KM.place(x=135, y=355)
End_of_the_day_KM.place(x=135, y=400)

# Text box lable
Execution_date_lable = Label(App, text="Execution date :")
Customer_name_lable  = Label(App, text="Customer name :")
City_lable  = Label(App, text="City : ")
Serial_number_lable  = Label(App, text="Serial number :")
Date_of_submission_of_the_report_lable  = Label(App, text="Date of submission of the report :")
Sum_of_appraisals_lable  = Label(App, text="Sum of appraisals :")
Start_of_the_day_KM_lable = Label(App, text="Start of the day KM :")
End_of_the_day_KM_lable = Label(App, text="End of the day KM :")

# Text box lable placement
Execution_date_lable.place(x=135, y=65)
Customer_name_lable.place(x=135, y=110)
City_lable.place(x=135, y=155)
Serial_number_lable.place(x=135, y=200)
Date_of_submission_of_the_report_lable.place(x=135, y=245)
Sum_of_appraisals_lable.place(x=135, y=290)
Start_of_the_day_KM_lable.place(x=135, y=335)
End_of_the_day_KM_lable.place(x=135, y=380)

# Submit button
Button_1 = Button(App, text="Submit Data", command=submit, width="31", height="2", bg="black", fg="black", font="10")
Button_1.place(x=135, y=434)

# delete data
Button_2 = Button(App, text="Delete all data",command=Delete_data, width="31", height="1",bg = "black", fg="red", font="10")
Button_2.place(x=135, y=484)

# Sum profit
Button_3 = Button(App, text="Sum profit", command=Sum_profit, width="20", height="1", bg="black", fg="black", font="10")
Button_3.place(x=135, y=524)

# Sum appraisals
Button_4 = Button(App,text="Sum appraisals",command=Sum_appraisals, width="20", height="1", bg="black", fg="black", font="10")
Button_4.place(x=135, y=564)

# Sum KM 
Button_5 = Button(App,text="Sum KM",command=Sum_KM, width="20", height="1", bg="black", fg="black", font="10")
Button_5.place(x=135, y=604)

conn.commit()
conn.close()
App.mainloop()
