# Import the required libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests


import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.attributes('-fullscreen', True)
#win.geometry("800x480")

def show_gang():
   url ="http://192.168.1.10:8080/json.htm?type=command&param=switchscene&idx=12&switchcmd=Toggle"
   resp = requests.get(url,  verify=False)

# Define a function to show the popup message
def show_msg():
   url ="http://192.168.1.10:8080/json.htm?type=command&param=switchlight&idx=44&switchcmd=Toggle"
   resp = requests.get(url,  verify=False)
 #  print (resp.status_code)
 #  print (resp.text)
   message=resp.text
   messagebox.showinfo("Message", message )

   # Define a function to show the popup message
def show_msg1():
   url ="http://192.168.1.10:8080/json.htm?type=command&param=switchlight&idx=44&switchcmd=Toggle"
   resp = requests.get(url,  verify=False)
#   message=resp.status_code
#   messagebox.showinfo("Message", message )

def show_msg2():
   url ="http://192.168.1.10/json.htm?type=command&param=switchscene&idx=1&switchcmd=Off"
   resp = requests.get(url,  verify=False)
#   message=resp.status_code
#   messagebox.showinfo("Message", message )

# Add an optional Label widget
Label(win, text= "Gouwzee 4", font= ('Aerial 17 bold italic')).pack(pady= 30)

# Create a Button to display the message
#ttk.Button(win, text= "Click Here", command=show_msg).pack(pady= 20)
ttk.Button(win, text= "WC aan/uit", command=show_msg1).pack(pady= 30)
ttk.Button(win, text= "Gang aan/uit", command=show_gang).pack(pady= 30)
#ttk.Button(win, text= "Beneden uit", command=show_msg2).pack(pady= 35)
win.mainloop()