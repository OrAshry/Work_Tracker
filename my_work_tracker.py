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
conn = sqlite3.connect("Work Database.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data (Execution_date text, Customer_name text, City text, Serial_number text,"
          "Date_of_submission_of_the_report  text, Sum_of_appraisals text, Profit_before_tax text,"
          "Start_of_the_day_KM text, End_of_the_day_KM text, KM_per_day text)")

# Submit data function
def submit():
    promil = 0.00035

    # Insert info to the database
    conn = sqlite3.connect("Work Database.db")
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES (:Execution_date, :Customer_name, :City, :Serial_number,"
              ":Date_of_submission_of_the_report, :Sum_of_appraisals, :Profit_before_tax ,"
              ":Start_of_the_day_KM, :End_of_the_day_KM, :KM_per_day)",
              {
                    'Execution_date': Execution_date.get(),
                    'Customer_name': Customer_name.get(),
                    'City': City.get(),
                    'Serial_number': Serial_number.get(),
                    'Date_of_submission_of_the_report': Date_of_submission_of_the_report.get(),
                    'Sum_of_appraisals': Sum_of_appraisals.get(),
                    'Profit_before_tax': promil * float(Sum_of_appraisals.get()),
                    'Start_of_the_day_KM': Start_of_the_day_KM.get(),
                    'End_of_the_day_KM': End_of_the_day_KM.get(),
                    'KM_per_day': float(End_of_the_day_KM.get()) - float(Start_of_the_day_KM.get()),
              })


    # Clear input box
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
def delete_data():
    conn = sqlite3.connect("Work Database.db")
    c = conn.cursor()
    c.execute("DELETE from data")
    conn.commit()
    conn.close()    


# Sum_profit function
pick_a_month_profit = Entry(App, width=15, highlightthickness=2, highlightbackground="black")
pick_a_month_profit.place(x=300, y=603)
def sum_profit() :
    conn = sqlite3.connect("Work Database.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Profit_before_tax) FROM data WHERE substr(Execution_date,4 ,2) = :The_month_she_choose",
              {'The_month_she_choose': pick_a_month_profit.get()})
    fetch_data_profit = c.fetchone()[0]
    print_fetch_data = "Sum of profit: " + str(fetch_data_profit) + " ILS"
    summary_label = Label(App, text=print_fetch_data)
    summary_label.place(x=200, y=730)
    #Clear input box
    pick_a_month_profit.delete(0, END)
    conn.commit()
    conn.close() 


# Sum appraisals function
pick_a_month_appraisals = Entry(App, width=15, highlightthickness=2, highlightbackground="black")
pick_a_month_appraisals.place(x=300, y=643)
def sum_appraisals():
    conn = sqlite3.connect("Work Database.db")
    c = conn.cursor()
    c.execute("SELECT SUM(Sum_of_appraisals) FROM data WHERE substr(Execution_date, 4, 2) = :The_month_she_choose",
              {'The_month_she_choose': pick_a_month_appraisals.get()})
    fetch_data_appraisals = c.fetchone()[0]
    print_fetch_data = "Sum of appraisals: " + str(fetch_data_appraisals) + " ILS"
    summary_label = Label(App, text=print_fetch_data)
    summary_label.place(x=200, y=730)
    # Clear input box
    pick_a_month_appraisals.delete(0, END)
    conn.commit()
    conn.close() 


# Sum KM function
pick_a_month_km = Entry(App, width=15, highlightthickness=2, highlightbackground="black")
pick_a_month_km.place(x=300, y=683)
def sum_km():
    conn = sqlite3.connect("Work Database.db")
    c = conn.cursor()
    c.execute("SELECT SUM(KM_per_day) FROM data WHERE substr(Execution_date, 4, 2) = :The_month_she_choose",
              {'The_month_she_choose': pick_a_month_km.get()})
    fetch_data_km = c.fetchone()[0]
    print_fetch_data = "Sum KM driven: " + str(fetch_data_km) + " KM"
    summary_label = Label(App, text=print_fetch_data)
    summary_label.place(x=200, y=730)
    # Clear input box
    pick_a_month_km.delete(0, END)
    conn.commit()
    conn.close() 


# Text box function
Execution_date = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
Customer_name = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
City = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
Serial_number = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
Date_of_submission_of_the_report = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
Sum_of_appraisals = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
Start_of_the_day_KM = Entry(App, width=34, highlightthickness=2, highlightbackground="black")
End_of_the_day_KM = Entry(App, width=34, highlightthickness=2, highlightbackground="black")


# Text box Placement
Execution_date.place(x=135, y=75)
Customer_name.place(x=135,y=130)
City.place(x=135, y=185)
Serial_number.place(x=135, y=240)
Date_of_submission_of_the_report.place(x=135, y=295)
Sum_of_appraisals.place(x=135, y=350)
Start_of_the_day_KM.place(x=135, y=405)
End_of_the_day_KM.place(x=135, y=460)


# Text box label
Execution_date_label = Label(App, text="Execution date :")
Customer_name_label  = Label(App, text="Customer name :")
City_label  = Label(App, text="City : ")
Serial_number_label  = Label(App, text="Serial number :")
Date_of_submission_of_the_report_label  = Label(App, text="Date of submission of the report :")
Sum_of_appraisals_label  = Label(App, text="Sum of appraisals :")
Start_of_the_day_KM_label = Label(App, text="Start of the day KM :")
End_of_the_day_KM_label = Label(App, text="End of the day KM :")


# Text box label placement
Execution_date_label.place(x=135, y=50)
Customer_name_label.place(x=135, y=105)
City_label.place(x=135, y=160)
Serial_number_label.place(x=135, y=215)
Date_of_submission_of_the_report_label.place(x=135, y=270)
Sum_of_appraisals_label.place(x=135, y=325)
Start_of_the_day_KM_label.place(x=135, y=380)
End_of_the_day_KM_label.place(x=135, y=435)


# Submit button
Button_1 = Button(App, text="Submit Data", command=submit, width="40", height="3", bg="black", fg="black", font="10")
Button_1.place(x=135, y=500)


# delete data
Button_2 = Button(App, text="Delete all data", command=delete_data, width="40", height="2",bg = "black",
                  fg="red", font="10")
Button_2.place(x=135, y=550)


# Sum profit
Button_3 = Button(App, text="Sum profit", command=sum_profit, width="15", height="2", bg="black", fg="black", font="10")
Button_3.place(x=135, y=600)


# Sum appraisals
Button_4 = Button(App,text="Sum appraisals", command=sum_appraisals, width="15", height="2", bg="black",
                  fg="black", font="10")
Button_4.place(x=135, y=640)


# Sum KM 
Button_5 = Button(App,text="Sum KM", command=sum_km, width="15", height="2", bg="black", fg="black", font="10")
Button_5.place(x=135, y=680)


conn.commit()
conn.close()
App.mainloop()
