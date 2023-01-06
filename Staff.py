import tkinter as tk

#window set up
root = tk.Tk() 
root.title('Restaurant System-Staff')
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#label set up
lbl_1 = tk.Label(root, relief = "ridge")
lbl_1.place(x=20,y=40,width=426,height=447)
lbl_2 = tk.Label(root, relief = "ridge")
lbl_2.place(x=460,y=40,width=120,height=447)
lbl_3 = tk.Label(root, bg = "yellow", text='Table State', fg='black', font=('Arial', 20), anchor='center')
lbl_3.place(x=20,y=10,width=426,height=30)
lbl_4 = tk.Label(root, bg = "yellow", text='Pounch', fg='black', font=('Arial', 20), anchor='center')
lbl_4.place(x=460,y=10,width=120,height=30)
lbl_5 = tk.Label(root, text = 'Table 1', font = ('Arial', 16))
lbl_5.place(x=90,y=110,width=70,height=35)
lbl_6 = tk.Label(root, text = 'Table 2', font = ('Arial', 16))
lbl_6.place(x=90,y=150,width=70,height=35)
lbl_7 = tk.Label(root, text = 'Table 3', font = ('Arial', 16))
lbl_7.place(x=90,y=190,width=70,height=35)

#table state
sets=("Available","Using","Need Clean")

#change table state
var1=tk.StringVar(root) 
var2=tk.StringVar(root) 
var3=tk.StringVar(root) 
var1.set("Available")
var2.set("Available")
var3.set("Available")

#show table state
opm_1=tk.OptionMenu(root, var1, *sets)
opm_1.place(x=180,y=110,width=100,height=35)
opm_2=tk.OptionMenu(root, var2, *sets)
opm_2.place(x=180,y=150,width=100,height=35)
opm_3=tk.OptionMenu(root, var3, *sets)
opm_3.place(x=180,y=190,width=100,height=35)

#show succeed message
def succeed():
    lbl_1 = tk.Label(root, text="pounch \n successfully")
    lbl_1.place(x=480,y=100,width=80,height=120)

#press list button to open the window for change list
def changeList():
    newWindow = tk.Toplevel(root)
    newWindow.title('Change List')
    width=600
    height=500
    screenwidth = newWindow.winfo_screenwidth()
    screenheight = newWindow.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    newWindow.geometry(alignstr)
    newWindow.resizable(width=False, height=False)

    #delete selected table
    def delete():
        selectedPlace = mylistbox.curselection()
        mylistbox.delete(selectedPlace)

        #menu for adding
    def menuselect():
        for i in checkboxes:
            if checkboxes[i].get() ==True:
                selectedbox.append(dish[i])
        showList()
        selectedbox.clear()
        mylistbox.place(x=60,y=90,width=212,height=314)

    #label set up
    lbl_nowList = tk.Label(newWindow, text='Now List', bg='yellow', font=('Arial', 20))
    lbl_nowList.place(x=20,y=30,width=291,height=30)
    lbl_bg1 = tk.Label(newWindow, relief = "ridge")
    lbl_bg1.place(x=20,y=60,width=291,height=423)
    lbl_addList = tk.Label(newWindow, text='Add List', bg='yellow', font=('Arial', 20))
    lbl_addList.place(x=330,y=30,width=250,height=30)
    lbl_bg2 = tk.Label(newWindow, relief = "ridge")
    lbl_bg2.place(x=330,y=60,width=251,height=422)

    #button set up
    bt_delete = tk.Button(newWindow, text='delete', font=('Arial', 15), command=delete)
    bt_delete.place(x=130,y=430,width=73,height=33)
    bt_add = tk.Button(newWindow, text='add', font=('Arial', 15), command=menuselect)
    bt_add.place(x=420,y=430,width=73,height=32)


    dish = {0:"Strawberry",1: "Peach",2:"mango",3:"Cherry"}
    checkboxes = {}

    j = 0
    for i in range (len (dish)):
        checkboxes[i] = tk.BooleanVar()
        Cb = tk.Checkbutton(newWindow, text=dish[i], variable=checkboxes[i])
        Cb.place(x=410,y=90+j,width=100,height=25)
        j += 40

    #make a listbox
    mylistbox = tk.Listbox(newWindow)
    selectedbox = []

    def showList():
        for i in selectedbox:
            mylistbox.insert(tk.END, i)
        mylistbox.place(x=60,y=90,width=212,height=314)
    showList()

#button set up
bt_1 = tk.Button(root, text='pounch in', font=('Arial', 12), command=succeed)
bt_1.place(x=478,y=400,width=88,height=30)
bt_2 = tk.Button(root, text='pounch out', font=('Arial', 12), command=succeed)
bt_2.place(x=478,y=440,width=88,height=30)
bt_3 = tk.Button(root, text = 'List', font = ('Arial, 12'), command=changeList)
bt_3.place(x=300,y=110,width=34,height=35)
bt_4 = tk.Button(root, text = 'List', font = ('Arial, 12'), command=changeList)
bt_4.place(x=300,y=150,width=34,height=35)
bt_5 = tk.Button(root, text = 'List', font = ('Arial, 12'), command=changeList)
bt_5.place(x=300,y=190,width=34,height=35)

root.mainloop()