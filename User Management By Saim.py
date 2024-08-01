import tkinter as tk

root=tk.Tk()

root.title("User Management By Muhammad Saim Sajid")

frame=tk.Frame(root)

frame.pack()

label1=tk.Label(frame,text="Enter Your Enrollment Number:")

label1.pack()

enroll=tk.Entry(frame)

enroll.pack()

label2=tk.Label(frame,text="Enter Your Password:")

label2.pack()

passw=tk.Entry(frame,show="*")

passw.pack()

checkbutton1=tk.Checkbutton(frame,text="Student")

checkbutton1.pack()

checkbutton2=tk.Checkbutton(frame,text="Employee")

checkbutton2.pack()

checkbutton3=tk.Checkbutton(frame,text="Applicant")

checkbutton3.pack()

vendortext=tk.Label(frame,text="If You Are A Vendor Then Type What You Supply Otherwise Write Nothing")

vendortext.pack()

vendorentry=tk.Entry(frame)

vendorentry.pack()

lablestudent=tk.Label(frame,text="List Of Things Student Can Access:")

lablestudent.pack()

studentlist=tk.Listbox(frame,height=5)

studentlist.insert(1,"Result")

studentlist.insert(2,"Fee")

studentlist.insert(3,"Courses")

studentlist.pack()

lableemployee=tk.Label(frame,text="List Of Things Employee Can Access:")

lableemployee.pack()

employeelist=tk.Listbox(frame,height=5)

employeelist.insert(1,"Salary")

employeelist.insert(2,"Schedule")

employeelist.insert(3,"Events")

employeelist.pack()

lableapplicant=tk.Label(frame,text="List Of Things Applicant Can Access:")

lableapplicant.pack()

applicantlist=tk.Listbox(frame,height=5)

applicantlist.insert(1,"Entry Test")

applicantlist.insert(2,"Merit List")

applicantlist.insert(3,"Schedule")

applicantlist.pack()

lableteacher=tk.Label(frame,text="If You are a teacher then select your course")

lableteacher.pack()

teachstring=tk.StringVar()

teachoption=tk.OptionMenu(frame,teachstring,"Sir Nauman","Sir Rafaqat Kazmi","Ma'am Sunnia","Ma'am Alisha Fida","Sir Umair","Muhammad Zafar")

teachoption.pack()
def infoentered(event):
    print("Information Stored")

Enter=tk.Button(frame,text="Enter Information")

Enter.pack()
Enter.bind("<Button-3>", infoentered)
menubar1=tk.Menu(root)

root.config(menu=menubar1)

exitmenu=tk.Menu(menubar1,tearoff=0)

exitmenu.add_command(label="Exit",command=root.destroy)

def vis():
    print("Visual Programming")


def web():
    print("web")


menubar1.add_cascade(label="File",menu=exitmenu)

menubutton1=tk.Menubutton(frame,text="Course")

menubutton1.pack()

menubutton2=tk.Menu(menubutton1,tearoff=0)

menubutton2.add_command(label="Visual Programming",command=vis)

menubutton2.add_command(label="Web",command=web)

menubutton1["menu"] = menubutton2



tk.mainloop()