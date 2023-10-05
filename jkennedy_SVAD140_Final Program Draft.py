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


import tkinter as tk

window = tk.Tk()

main_frm = tk.Frame(width=50)
wel_label = tk.Label(text="Welcome to the Club Kid Tracker")
wel_label.pack()

btn_Check_in = tk.Button(
    text="CHECK IN",
    height=3)
btn_Check_in.pack(fill=tk.X)

btn_Check_out = tk.Button(
    text="CHECK OUT",
    height=3)
btn_Check_out.pack(fill=tk.X)

btn_current_attendance = tk.Button(
    text="CURRENT ATTENDANCE",
    height=3)
btn_current_attendance.pack(fill=tk.X)

btn_create_member = tk.Button(
    text="CREATE MEMBER",
    height=3)
main_frm.pack()

btn_create_member.pack(fill=tk.X)
btm_frm = tk.Frame(height=20)
btm_frm.pack()

member = str()
##member.fname()
##member.lname()
##member.pin()
##member.checkedin()
##member.timestamp()

##def check_in():
##def check_out():
##def current_attendance():
##def create_member():
window.mainloop()
