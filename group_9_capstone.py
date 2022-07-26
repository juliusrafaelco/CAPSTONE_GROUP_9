import json
import pandas as pd
import re
import pymongo
from datetime import datetime
from pymongo import MongoClient
from tkinter import * 

#CREATES and modifies the GUI
root = Tk()
root.title("Income Tracker")
#creates the text entry in GUI #Data Inputs
f_name =  Entry(root, width = 30,)
f_name.grid(row=0, column=1, padx=20)

f_current_income = Entry(root, width = 30,)
f_current_income.grid(row=1, column=1, padx=20)

f_month_entry =  Entry(root, width = 30,)
f_month_entry.grid(row=2, column=1, padx=20)

f_expenses =  Entry(root, width = 30,)
f_expenses.grid(row=3, column=1, padx=20)

f_expected_monthly_earnings =  Entry(root, width = 30,)
f_expected_monthly_earnings.grid(row=4, column=1, padx=20)

f_savings_goal =  Entry(root, width = 30,)
f_savings_goal.grid(row=5, column=1, padx=20)

#create text box labels
#Format for each entry: Name, Current Income, Expected Monthly Earning, target savings, expenses(list)

#codes to be excuted when SUBMIT button is pressed
def submit():
    
    #reassigning values obtain from input function to easier variable names
    name = f_name.get()
    month = f_month_entry.get()
    current_income = f_current_income.get()
    expearning= f_expected_monthly_earnings.get()
    targetsave= f_savings_goal.get()
    expense = f_expenses.get()
    month_number=0

    #for y in month:
        #mnum = datetime.strptime(y, '%B').month
        #month_number.append(mnum)
    #determines the month number of the month
    if month == "January":
        month_number += month_number+1
    elif month == "February":
        month_number += month_number+2
    elif month == "March":
        month_number += month_number+3
    elif month == "April":
        month_number += month_number+4
    elif month == "May":
        month_number += month_number+5
    elif month == "June":
        month_number += month_number+6
    elif month == "July":
        month_number += month_number+7
    elif month == "August":
        month_number += month_number+8
    elif month == "September":
        month_number += month_number+9
    elif month == "October":
        month_number += month_number+10
    elif month == "November":
        month_number += month_number+11
    elif month == "December":
        month_number += month_number+12
        
    money = current_income + expearning

    suggestions = ['You have extra money', 'You will not reach your savings goal', 'You have exceeded your current income']
    
    #gives the recommendation based on the amount of money left
    recos=[]
    if expense > money:
        recs = suggestions[2]
        recos.append(recs)
    elif expense == money:
        recs = suggestions[1]
        recos.append(recs)
    else:
        recs = suggestions[0]
        recos.append(recs)

    rsave = round(int(targetsave)/(12-month_number))
    #creates a dictionary for the database
    diction={'Name':name,'Month of Input':str(month),'Current Income':current_income,
       'Expected Earning for the Month': expearning, 'Target Yearly Savings':targetsave,
       'Monthly Expenses': expense,'Money Available':money,'Recommendation':recos,'Recommended Monthly Savings': rsave}
    #CREATES LABEL
    f_recommendation_label = Label(root, text=recos)
    f_recommendation_label.grid(row=0, column=3, padx=20)
    
    f_money_availables_label = Label(root, text=money)
    f_money_availables_label.grid(row=1, column=3, padx=20)
    
    f_recommended_monthly_savingss_label = Label(root, text = rsave)
    f_recommended_monthly_savingss_label.grid(row=2, column=3, padx = 20)

# creation of MongoClient
    client=MongoClient()
  
 # Connect with the portnumber and host
    client = MongoClient('mongodb://localhost:27017')
  
 # Access database
    mydatabase = client['capstonedata']
  
 # Access collection of the database
    mycollection=mydatabase['myTables']
  
 # dictionary to be added in the database
    data = diction
  
 # inserting the data in the database
    data = mydatabase.myTables.insert_one(data)
    
#chunk of code to be executed when PREVIOUS RECORD Button is pressed
def query():
    client = MongoClient('mongodb://localhost:27017')

    db = client.capstonedata
  
    # Created or Switched to collection names: myTable
    collection = db.myTables
  
    # To find() all the entries inside collection name 'myTable'
    cursor = collection.find()
    for record in cursor:
        print(record)
        
#creates label in the GUI
f_name_label = Label(root, text="Name:")
f_name_label.grid(row=0, column=0, padx=20)

f_current_income_label = Label(root, text="Current Income:")
f_current_income_label.grid(row=1, column=0, padx=20)

f_month_entry_label = Label(root, text="Month:")
f_month_entry_label.grid(row=2, column=0, padx=20)

f_expenses_label = Label(root, text="Expenses:")
f_expenses_label.grid(row=3, column=0, padx=20)

f_expected_monthly_earnings_label = Label(root, text="Expected Monthly Earnings:")
f_expected_monthly_earnings_label.grid(row=4, column=0, padx=20)

f_savings_goal_label = Label(root, text="Savings goal:")
f_savings_goal_label.grid(row=5, column=0, padx=20)

f_recommendations_label = Label(root, text="Recommedations:")
f_recommendations_label.grid(row=0, column=2, padx=20)

f_money_available_label = Label(root, text="Recommended Monthly Savings:" )
f_money_available_label.grid(row=1, column=2, padx=20)
    
f_money_available_label = Label(root, text="Money Left:")
f_money_available_label.grid(row=2, column=2, padx=20)


#submit button
submit_btn = Button(root, text="SUBMIT", command =submit)
submit_btn.grid(row = 6, column = 0, columnspan=2, pady = 2, padx = 10, ipadx = 100)

#query button
SHOW_btn = Button(root, text="Previous RECORD", command =query)
SHOW_btn.grid(row = 7, column = 0, columnspan=2, pady = 2, padx = 10, ipadx = 100)

#DEL_btn = Button(root, text="CLEAR DATA", command =perform)
#DEL_btn.grid(row = 8, column = 0, columnspan=2, pady = 2, padx = 10, ipadx = 100)
root.mainloop()

##### execute to delete data base
db.myTables.delete_many( { } )