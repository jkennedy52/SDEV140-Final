##Final Project
##James Kennedy SDEV 140
##Email: jkennedy52@ivytech.edu
##Club Kid Tracker Program

##Goals:
##Allow check in of members
##Allow check out of members
##Provide a way to see currently checked in members
##Do not allow a member to check in if they are already checked in
##Do not allow a member to check out if they are not checked in
##Record timestamps of when a memeber checked in our out


import tkinter as tk ##for gui
from tkinter import PhotoImage
from datetime import datetime ##for timestamp
from PIL import Image, ImageTk


##defining main window
window = tk.Tk()
window.title("Club Member Tracker")
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)
window.resizable(width=False, height=False)
window.geometry(f"+0+0")


##https://github.com/jkennedy52/SDEV140-Final/blob/2794b1031e117fd95200ba7db70a9acddf9863ad/green.png



##Defining variable information type
##fname = str()  ##First Name
##lname = str()  ##Last Name
##pin = int()    ##Members pin number
##tstamp = str() ##Last time stamp
statecheck = False  ##Will show if member is checked in (true) or out(false)
fnames = []
lnames = []
pins = []
timestamps = []
checks = []
green_check = Image.open("green.png")
red_x = Image.open("red.png")
green_photo = ImageTk.PhotoImage(green_check)
red_photo = ImageTk.PhotoImage(red_x)
transparent_image = PhotoImage(width=1, height=1)
pin_error = "Error with pin. Please try again."


##Creating Button Actions
def create():
    name1 = fname.get()
    name2 = lname.get()
    pin1 = pin.get()

    # Validate name and pin
    if not name1.isalpha():
        display_error("Invalid first name")
    elif not name2.isalpha():
        display_error("Invalid last name")
    elif not (pin1.isdigit() and 0 <= int(pin1) <= 9999):
        display_error("Invalid PIN")
    else:
        # Check for duplicate PIN
        if pin1 in pins:
            display_error("Duplicate PIN")
        else:
            # Data is valid, add the member
            fnames.append(name1)
            lnames.append(name2)
            pins.append(pin1)
            timestamps.append(datetime.now())
            checks.append(False)
            clear_text()
            image_label.config(image=green_photo)
            
def display_error(message):
    pin.delete(0, tk.END)
    pin.insert(0, message)
    image_label.config(image=red_photo)            
    
def checkin():
    pincheck = str(pin.get())
    for i in range(len(fnames)):
        if pincheck == pins[i]:
            if checks[i] != True:
                fname.insert(0, fnames[i])
                lname.insert(0,lnames[i])
                timestamps[i] = datetime.now()
                tstamp.config(text = timestamps[i])
                statecheck = True
                checks[i] = statecheck
                state.config(text="Checked In")
                image_label.config(image=green_photo)
            else:
                state.config(text="Already checked in!")
                image_label.config(image=red_photo)
        else:
            display_error("Invalid PIN")
                
def checkout():
    pincheck = str(pin.get())
    for i in range(len(fnames)):
        if pincheck == pins[i]:
            if checks[i] != False:
                fname.insert(0, fnames[i])
                lname.insert(0,lnames[i])
                timestamps[i] = datetime.now()
                tstamp.config(text = timestamps[i])
                statecheck = False
                checks[i] = statecheck
                state.config(text="Checked Out")
                image_label.config(image=green_photo)
            else:
                state.config(text="Not Checked In")
                image_label.config(image=red_photo)
        else:
            display_error("Invalid PIN")
              
                  
def current_attendance():
    window3 = tk.Tk()
    window3.title("Club Member Current Attendance")
    window3.resizable(width=False, height=False)
    window3.geometry(f"+480+200") 
    for i in range(len(fnames)):
        if checks[i] != False:
            att = tk.Label(master=window3, text=(fnames[i],lnames[i],timestamps[i]))
            att.grid(row=i, column=0, padx=1, pady=1)
    window.mainloop()
    
        

def clear_text():
    lname.delete(0,tk.END)
    fname.delete(0, tk.END)
    pin.delete(0, tk.END)
    tstamp.config(text="")
    state.config(text="")
    image_label.config(image=transparent_image)
        
      
##Start of the button side of our program
frm_btn = tk.Frame(master=window, relief=tk.RAISED)

btn_create_member = tk.Button(master=frm_btn,
    text="CREATE MEMBER",
    height=3,
     command=create)

btn_Check_in = tk.Button(master=frm_btn,
    text="CHECK IN",
    height=3,
    command=checkin)

btn_Check_out = tk.Button(master=frm_btn,
    text="CHECK OUT",
    height=3,
    command=checkout)

btn_current_attendance = tk.Button(master=frm_btn,
    text="CURRENT ATTENDANCE",
    height=3,
    command=current_attendance)

btn_clear = tk.Button(master=frm_btn,
                      text="CLEAR SCREEN",
                      height=3,
                      command=clear_text)

##line it all up
btn_create_member.grid(row=0, column = 0, padx=5,pady=5, sticky = "nesw")
btn_Check_in.grid(row=1, column=0, padx=5, pady=5, sticky = "nesw")
btn_Check_out.grid(row=2, column=0, padx=5, pady=5, sticky = "nesw")
btn_current_attendance.grid(row=3, column=0, padx=5, pady=5, sticky = "nesw")
btn_clear.grid(row=4, column=0, padx=5, pady=5, sticky = "nesw")
frm_btn.grid(row=0, column=0, padx=5, pady=5, sticky ="n")

##End of button side of program

##Start of Display side of the program
frm_display = tk.Frame(master=window, relief="sunken")
dir_label = tk.Label(master=frm_display, text="Welcome to the Club Member Tracker!", pady=10 )
fname_label = tk.Label(master=frm_display, text="First Name", width=10)
fname = tk.Entry(master=frm_display, text="", width = 30)
lname_label = tk.Label(master=frm_display, text="Last Name", width=10)
lname = tk.Entry(master=frm_display, text="", width = 30)
pin_label = tk.Label(master=frm_display, text="Pin", width=10)
pin = tk.Entry(master=frm_display, text="", width = 30)
tstamp_label = tk.Label(master=frm_display, text="Last Stamp", width=10)
tstamp = tk.Label(master=frm_display, text="null", width = 30)
state_label = tk.Label(master=frm_display, text="Status", width=10)
state = tk.Label(master=frm_display, text="null", width = 30)
image_label = tk.Label(master=window)

dir_label.grid(row=0, column=1, columnspan=2, sticky="nesw")
fname_label.grid(row=1,column=1, pady=5, padx=5)
fname.grid(row=1, column=2, pady=5)
lname_label.grid(row=2, column=1, padx=5, pady=5)
lname.grid(row=2, column=2, pady=5)
pin_label.grid(row=3, column=1, padx=5, pady=5)
pin.grid(row=3, column=2, pady=5)
tstamp_label.grid(row=4, column=1, padx=5, pady=5)
tstamp.grid(row=4, column=2, pady=5)
state_label.grid(row=5, column=1, padx=5, pady=5)
state.grid(row=5, column=2, pady=5)
image_label.grid(row=6, columnspan=2, pady=5)
frm_display.grid(row=0, column=1, padx=5, pady=5, sticky="n")


##Directions Window
window2 = tk.Toplevel(window)
window2.title("Club Member Tracker")

window2.geometry(f"+480+0")


window2.title("Tracker Directions")
directions_label = tk.Label(master=window2, text="Please follow the directions below: ", pady=10)

directions_text = tk.Text(window2, wrap=tk.WORD, width=150, height=7, bd=0)
directions_label.pack()
directions_text.pack()
directions = """
1. If you would like to create a new member enter the information into the boxes and then click the create member button.
    a. Pins need to be unique and a number between 0000 and 9999.
2. If you would like to check a member in then enter the members unique pin and click the check in button.
3. If you would like to check a member out enter the members unique pin and click the check out button.
4. If you would like to check the current members that are checked in click the current attendance button and you will see the list.
5. Make sure after each action that you click the clear button to make sure you are working with clean information.
"""
directions_text.insert(tk.END, directions)
window2.focus_set()
window.mainloop()
