import time
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk

#window set up
root = tk.Tk() 
root.title('餐廳系統-盈餘狀況介面')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#message set up
mes = '餐點\n狀況'
msg =tk.Message(root,text=mes,font=("Arial",18,"bold"), relief = "ridge",fg='#00CACA')
msg.place(x=20,y=70,width=300,height=330)

#message set up
mes = '員工\n薪水'
msg =tk.Message(root,text=mes,font=("Arial",18,"bold"), relief = "ridge",fg='#00CACA')
msg.place(x=340,y=70,width=240,height=330)

#label set up
lbl_title1 = tk.Label(root, text="員工薪資表", font=("Arial", 20), bg="#1E90FF")
lbl_title1.place(x=340,y=30,width=240,height=31)
lbl_title2 = tk.Label(root, text="餐點狀況", font=("Arial", 20), bg="#1E90FF")
lbl_title2.place(x=20,y=30,width=300,height=31)
lbl_sumIn = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumIn["text"] = "總收入\n" + str(1000)
lbl_sumIn.place(x=20,y=410,width=180,height=77)
lbl_sumOut = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumOut["text"] = "總支出 :\n" + str(700)
lbl_sumOut.place(x=210,y=410,width=180,height=77)
lbl_sumEarn = tk.Label(root, font = ("Arial", 15), relief="groove")
lbl_sumEarn["text"] = "盈餘 :\n" + str(300)
lbl_sumEarn.place(x=400,y=410,width=180,height=77)

root.mainloop()