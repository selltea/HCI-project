#Import the required Libraries
from tkinter import *
from tkinter import ttk
import time
import numpy as geek
from blue import search
import re
from tkinter import messagebox
#Create an instance of Tkinter frame
win = Tk()
#Set the geometry of Tkinter frame
win.geometry("750x270")

#def open_popup_DRIVER():
#   top= Toplevel(win)
#   top.geometry("750x250")
#   top.title("DRIVER ON THE ROAD")
#   top.resizable(False, False)
#   # Create Entry Widgets for HH MM SS
#   sec = StringVar()
#   Entry(top, textvariable=sec, width=2, font='Helvetica 14').place(x=220, y=120)
#   sec.set('00')
#   mins = StringVar()
#   Entry(top, textvariable=mins, width=2, font='Helvetica 14').place(x=180, y=120)
#   mins.set('00')
#   hrs = StringVar()
#   Entry(top, textvariable=hrs, width=2, font='Helvetica 14').place(x=142, y=120)
#   hrs.set('00')
#   # Define the function for the timer

#   def countdowntimer():
#      times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
#      while times > -1:
#         minute, second = (times // 60, times % 60)
#         hour = 0
#         if minute > 60:
#            hour, minute = (minute // 60, minute % 60)
#         sec.set(second)
#         mins.set(minute)
#         hrs.set(hour)
#         # Update the time
#         top.update()
#         time.sleep(1)
#         if (times == 0):
#            sec.set('00')
#            mins.set('00')
#            hrs.set('00')
#         times -= 1

#   Label(top, font=('Helvetica bold', 22), text='Set the Timer').place(x=105, y=70)
#   Button(top, text='START', bd='2', font=('Helvetica bold',10), command = countdowntimer).place(x=167, y=165)
def open_popup_REPORT():
   bluetooth= Toplevel(win)
   bluetooth.geometry("750x250")
   bluetooth.title("Reports")
   def foo():
      a = receive()
      Label(bluetooth, text = a).pack()
   def LOGIN():
      logged= Toplevel(win)
      logged.geometry("750x750")
      logged.title(chosen_device.get())
      logged.resizable(False, False)
      shepherd = chosen_device.get()
      chosentxt = "{}.txt".format(shepherd)
      def open_text():
         text_file = open(chosentxt, "r")
         content = text_file.read()
         profilenums=re.findall(r'\b\d+\b', content)
         
         my_text_box.delete('1.0', END)
         my_text_box.insert(END, content)
         text_file.close()
         text_file2 = open("car.txt", "r")
         content2 = text_file2.read()
         carnums=re.findall(r'\b\d+\b', content2)
         my_text_box2.delete('1.0', END)
         my_text_box2.insert(END, content2)
         text_file2.close()
         out_arr = []
         diff = "car is"
         for i in range(len(profilenums)):
            result = int(profilenums[i]) - int(carnums[i])
            if(result>=0):
               diff += " increasing by "+ str(abs(result))
            elif(result<0):
               diff += " decreasing by "+ str(abs(result))
            
            
            out_arr.append(result)
         messagebox.showinfo("car info", diff)
         
      

      def save_text():
         text_file = open(chosentxt, "w")
         text_file.write(my_text_box.get(1.0, END))
         text_file.close()
      def save_on_car():
         text_file = open("car.txt", "w")
         text_file.write(my_text_box.get(1.0, END))
         text_file.close()

# Creating a text box widget
      Label(logged, text="user profile", font=('Helvetica 14 bold')).pack(pady=20)
      my_text_box = Text(logged, height=10, width=20)
      my_text_box.pack()
      Label(logged, text="car settings", font=('Helvetica 14 bold')).pack(pady=20)
      my_text_box2 = Text(logged, height=10, width=20)
      my_text_box2.pack()
      open_btn = Button(logged, text="Open File", command=open_text)
      open_btn.pack()

# Create a button to save the text
      save = Button(logged, text="Save File", command=save_text)
      save.pack()
      save_car = Button(logged, text="override car settings", command=save_on_car)
      save_car.pack()
      #Label(logged, text= diff, font=('Helvetica 14 bold')).pack(pady=20)
      #def toggle():
      #   button1['text'] = toggle_text[button1['text']]
      #   button2['text'] = toggle_text[button2['text']]

      #toggle_text = {'Yes': 'OK',
      #         'No': 'Cancel'
      #         ,
      #         'OK': 'Yes',
      #        'Cancel': 'No'
      #         }
      #label = Label(logged , text='?')
      #textbox = Text(logged)
      #textbox.insert
      #button1 = Button(logged , text='Yes', command=toggle)
      #button2 = Button(logged , text='No', command=toggle)
      #label.pack(padx=20 , pady=5)
      #button1.pack( padx=10)
      #button2.pack( padx=10)

      #Label(logged, text="you have driven for 4 hours").pack()
   #label1 = Label(bluetooth, text = "").pack()
   ttk.Button(bluetooth, text = "search for devices", command = foo).pack()
   chosen_device = ttk.Entry(bluetooth)
   chosen_device.pack()
   ttk.Button(bluetooth, text = "use this device", command = LOGIN).pack()


def receive():
   devices=search()
   return devices

def connect():
   import cv2
   import mediapipe as mp
   import socket
   import pickle
   listensocket=socket.socket()
   Port=8000
   maxConnections=5
   IP=socket.gethostname()
   listensocket.bind((IP,Port))
   listensocket.listen(maxConnections)
   print("Server started at " + IP + " on port " + str(Port))
   clientsocket,address=listensocket.accept()
   data=listensocket.recv(1024)
   res = pickle.loads(data)
   print("New connection made!")
   

Label(win, text="choose the mode", font=('Helvetica 14 bold')).pack(pady=20)
#Create a button in the main Window to open the popup
#ttk.Button(win, text= "Driving", command= open_popup_DRIVER).pack()
ttk.Button(win, text= "Reports", command= open_popup_REPORT).pack()
win.mainloop()






























































































































