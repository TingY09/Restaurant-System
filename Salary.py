import tkinter as tk

#window set up
root = tk.Tk() 
root.title('Restaurant System-Salary Table')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#staff list
sets=("Tom","John","Mary", "Karen", "Jack")

#change staff
var1=tk.StringVar(root) 
var1.set("Staff List")

#show staff
opm_1=tk.OptionMenu(root, var1, *sets)
opm_1.place(x=130,y=50,width=354,height=30)

#Label set up
lbl_time = tk.Label(root,font=("Arial", 20))
lbl_salary=tk.Label(root, font=("Arial", 80))

#salary table
salary=[10000, 50, 60]

def showLastWeek():
    lbl_time["text"] = "Last Week Salary :"
    lbl_time.place(x=100,y=220,width=400,height=66)
    lbl_salary["text"] = salary[0]
    lbl_salary.place(x=160,y=320,width=294,height=80)
def showLastHalfMonth():
    lbl_time["text"] = "Last Half of Month Salary :"
    lbl_time.place(x=100,y=220,width=400,height=66)
    lbl_salary["text"] = salary[1]
    lbl_salary.place(x=160,y=320,width=294,height=80)
def showLastMonth():
    lbl_time["text"] = "Last Month Salary :"
    lbl_time.place(x=100,y=220,width=400,height=66)
    lbl_salary["text"] = salary[2]
    lbl_salary.place(x=160,y=320,width=294,height=80)

#Button set up
bt_lastWeek = tk.Button(root, text="Last Week", bg="#1E90FF",command=showLastWeek)
bt_lastWeek.place(x=140,y=120,width=78,height=61)
bt_lastHalfMonth = tk.Button(root, text="Last Half \nof Month", bg="#1E90FF", command=showLastHalfMonth)
bt_lastHalfMonth.place(x=270,y=120,width=78,height=60)
bt_lastMonth = tk.Button(root, text="Last Month", bg="#1E90FF", command=showLastMonth)
bt_lastMonth.place(x=400,y=120,width=78,height=61)

root.mainloop()