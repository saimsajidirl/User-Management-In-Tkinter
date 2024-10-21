# User-Management-In-Tkinter

Documentation for User Management Application using Tkinter

This script creates a user interface (UI) for a User Management System using Python's tkinter library. The application allows users to enter their enrollment number, password, role (student, employee, or applicant), and, if relevant, specify the type of supply if they are a vendor. Additionally, it lists the access rights of each role (student, employee, and applicant) and allows teachers to select their courses.
Overview:

    Roles: Students, Employees, Applicants, and Vendors.
    UI Components:
        Text entry fields for enrollment number, password, and vendor information.
        Checkbuttons to select the role (student, employee, applicant).
        Listboxes to show the different things that each role can access.
        Dropdown (OptionMenu) for selecting a course if the user is a teacher.
        A button to enter the information and a menu bar with an option to exit the application.

Detailed Walkthrough of the Code:
1. Tkinter Root Window:

The application starts by creating a root window using Tkinter. This window will house all other widgets (buttons, labels, etc.).

python

root = tk.Tk()
root.title("User Management By Muhammad Saim Sajid")

2. Frame:

A Frame is created to group all the widgets together and make them easier to manage and organize within the window.

python

frame = tk.Frame(root)
frame.pack()

3. Labels and Entry Fields:

    Enrollment Number: A Label and an Entry field for the user to enter their enrollment number.
    Password: A Label and an Entry field (with show="*" to mask the input) for entering the password.

python

label1 = tk.Label(frame, text="Enter Your Enrollment Number:")
label1.pack()

enroll = tk.Entry(frame)
enroll.pack()

label2 = tk.Label(frame, text="Enter Your Password:")
label2.pack()

passw = tk.Entry(frame, show="*")
passw.pack()

4. Role Selection (Checkbuttons):

The user can select one or more roles (student, employee, applicant) using Checkbuttons. Each role will grant access to different functionalities within the system.

python

checkbutton1 = tk.Checkbutton(frame, text="Student")
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(frame, text="Employee")
checkbutton2.pack()

checkbutton3 = tk.Checkbutton(frame, text="Applicant")
checkbutton3.pack()

5. Vendor Information:

If the user is a vendor, they can specify what they supply using the Entry field.

python

vendortext = tk.Label(frame, text="If You Are A Vendor Then Type What You Supply Otherwise Write Nothing")
vendortext.pack()

vendorentry = tk.Entry(frame)
vendorentry.pack()

6. Access Rights (Listboxes):

The application shows what each role can access through a Listbox. There are three listboxes, one for each role: Student, Employee, and Applicant. Items can be added to these listboxes using the insert() method.

python

lablestudent = tk.Label(frame, text="List Of Things Student Can Access:")
lablestudent.pack()

studentlist = tk.Listbox(frame, height=5)
studentlist.insert(1, "Result")
studentlist.insert(2, "Fee")
studentlist.insert(3, "Courses")
studentlist.pack()

lableemployee = tk.Label(frame, text="List Of Things Employee Can Access:")
lableemployee.pack()

employeelist = tk.Listbox(frame, height=5)
employeelist.insert(1, "Salary")
employeelist.insert(2, "Schedule")
employeelist.insert(3, "Events")
employeelist.pack()

lableapplicant = tk.Label(frame, text="List Of Things Applicant Can Access:")
lableapplicant.pack()

applicantlist = tk.Listbox(frame, height=5)
applicantlist.insert(1, "Entry Test")
applicantlist.insert(2, "Merit List")
applicantlist.insert(3, "Schedule")
applicantlist.pack()

7. Teacher Selection:

If the user is a teacher, they can select their course using an OptionMenu. The available courses are provided in a dropdown list.

python

lableteacher = tk.Label(frame, text="If You are a teacher then select your course")
lableteacher.pack()

teachstring = tk.StringVar()
teachoption = tk.OptionMenu(frame, teachstring, "Sir Nauman", "Sir Rafaqat Kazmi", "Ma'am Sunnia", "Ma'am Alisha Fida", "Sir Umair", "Muhammad Zafar")
teachoption.pack()

8. Information Entry Button:

A button is provided to allow the user to "Enter Information". The button uses the bind() method to listen for a right-click event (<Button-3>) to trigger the action of storing the entered information.

python

def infoentered(event):
    print("Information Stored")

Enter = tk.Button(frame, text="Enter Information")
Enter.pack()
Enter.bind("<Button-3>", infoentered)

9. Menu Bar:

The application has a menu bar with a file menu. The "Exit" option closes the application when selected. Additionally, a Menubutton is created to provide access to two courses (Visual Programming and Web) via submenus.

python

menubar1 = tk.Menu(root)
root.config(menu=menubar1)

exitmenu = tk.Menu(menubar1, tearoff=0)
exitmenu.add_command(label="Exit", command=root.destroy)

menubar1.add_cascade(label="File", menu=exitmenu)

def vis():
    print("Visual Programming")

def web():
    print("web")

menubutton1 = tk.Menubutton(frame, text="Course")
menubutton1.pack()

menubutton2 = tk.Menu(menubutton1, tearoff=0)
menubutton2.add_command(label="Visual Programming", command=vis)
menubutton2.add_command(label="Web", command=web)

menubutton1["menu"] = menubutton2

10. Main Loop:

Finally, the script enters the Tkinter event loop with tk.mainloop(), which keeps the window open and listens for user input.

python

tk.mainloop()

Functionality Overview:

    User Input: The user can input their enrollment number, password, select their role, and specify vendor details.
    Role-based Access: Each role (Student, Employee, Applicant) has a list of items they can access, which is displayed in the respective Listbox.
    Teacher Selection: Teachers can select their course using a dropdown (OptionMenu).
    Menu Options: The menu includes an option to exit the application and additional options for courses (Visual Programming and Web).

How It Works:

    User selects a role: Student, Employee, or Applicant.
    User enters their details: Enrollment number, password, and optionally vendor information if they are a vendor.
    Access rights and selection: Based on the role, the user can view the access rights associated with that role. If the user is a teacher, they can select the course they teach.
    Menu interaction: The user can interact with the "Course" menu to select between "Visual Programming" and "Web".
    Exit: The user can click on the "Exit" option in the menu to close the application.
