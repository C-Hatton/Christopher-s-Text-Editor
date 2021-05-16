#Made by Christopher Hatton (558)

# -*-coding: utf-8-*-

from tkinter import *            #for Tk window
import tkinter as tk             #to make Frame
from tkinter import scrolledtext #to create textbox
from tkinter import filedialog   #to open and choose documents
from sys import platform         #to make sure that the os is win32
import ctypes                    #to make sure that the screen size is large enough
import os                        #to allow help button open help web page

name = "Christopher's Text Editor"

def f_main():

    #START:
    root = tk.Tk()

    root.state('zoomed')
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    root.bind('<F10>', lambda event: root.state('zoomed'))
    root.bind('<F9>', lambda event: root.destroy)
    root.title(name) #Sets the title of the window

    #Make global variables:
    file_location_save = ['']
    file_open = [False] 
    file_open_name = ['']
    file_types_name = 'Text files'
    file_types = 'txt,py,html,htm'

    def f_open_file(): #Open files:
        file_location = ''
        file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file location (local variable)
        file_location_save[0] = file_location #Puts the file location in it's global variable
        while True:
            try:
                f = open(file_location,'r') #Opens the file
            except FileNotFoundError:
                break
            else:
                contents = f.read() #Reads the file
                f.close() #Closes the file
                textbox.delete("1.0","end")
                textbox.insert("end-1c",contents) #Puts the contents of the file in the textbox
                x = []
                x = file_location.split('/') #Gets the name of the file(local variable)
                file_open_name[0] = x[-1] #Puts the file name in it's global variable
                file_open[0] = 'True' #File has been opened (useful)
                root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                break

    def f_open_file_key(event): #Open files:
        file_location = ''
        file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file location (local variable)
        file_location_save[0] = file_location #Puts the file location in it's global variable
        while True:
            try:
                f = open(file_location,'r') #Opens the file
            except FileNotFoundError:
                break
            else:
                contents = f.read() #Reads the file
                f.close() #Closes the file
                textbox.delete("1.0","end")
                textbox.insert("end-1c",contents) #Puts the contents of the file in the textbox
                x = []
                x = file_location.split('/') #Gets the name of the file(local variable)
                file_open_name[0] = x[-1] #Puts the file name in it's global variable
                file_open[0] = 'True' #File has been opened (useful)
                root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                break

    def f_save_file(): #Save files:
        if file_open[0] == 'True':
            #If one or more file has beened opened:
            x = file_location_save[0]
            f = open(x,'w')
            f.write(textbox.get("1.0",'end-1c')) #Saves file to the opened file
            f.close()
        else:
            #If no files been opened:
            file_location = ''
            file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file to save to (local variable)
            file_location_save[0] = file_location  #Puts the file location in it's global variable
            while True:
                try:
                    f = open(file_location,'w') 
                except FileNotFoundError:
                    break
                else:
                    f.write(textbox.get("1.0",'end-1c')) #Saves the file
                    f.close()
                    file_open[0] = True #File has been opened
                    x = []
                    x = file_location.split('/') #Gets the name of the file(local variable)
                    file_open_name[0] = x[-1] #Puts it in a global variable
                    root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                    break

    def f_save_file_key(event): #Save files:
            if file_open[0] == 'True':
                #If one or more file has beened opened:
                x = file_location_save[0]
                f = open(x,'w')
                f.write(textbox.get("1.0",'end-1c')) #Saves file to the opened file
                f.close()
            else:
                #If no files been opened:
                file_location = ''
                file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file to save to (local variable)
                file_location_save[0] = file_location  #Puts the file location in it's global variable
                while True:
                    try:
                        f = open(file_location,'w') 
                    except FileNotFoundError:
                        break
                    else:
                        f.write(textbox.get("1.0",'end-1c')) #Saves the file
                        f.close()
                        file_open[0] = True #File has been opened
                        x = []
                        x = file_location.split('/') #Gets the name of the file(local variable)
                        file_open_name[0] = x[-1] #Puts it in a global variable
                        root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                        break

    def f_save_as(): #Save file as:
        file_location = ''
        file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file to save to (local variable)
        file_location_save[0] = file_location  #Puts the file location in it's gloval variable
        while True:
            try:
                f = open(file_location,'w') 
            except FileNotFoundError:
                break
            else:
                f.write(textbox.get("1.0",'end-1c')) #Saves the file
                f.close()
                file_open[0] = True #File has been opened
                x = []
                x = file_location.split('/') #Gets the name of the file(local variable)
                file_open_name[0] = x[-1] #Puts it in a global variable
                root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                break

    def f_save_as_key(event): #Save file as:
        file_location = ''
        file_location = filedialog.askopenfilename(filetypes=((file_types_name,file_types),)) #Gets the file to save to (local variable)
        file_location_save[0] = file_location  #Puts the file location in it's gloval variable
        while True:
            try:
                f = open(file_location,'w') 
            except FileNotFoundError:
                break
            else:
                f.write(textbox.get("1.0",'end-1c')) #Saves the file
                f.close()
                file_open[0] = True #File has been opened
                x = []
                x = file_location.split('/') #Gets the name of the file(local variable)
                file_open_name[0] = x[-1] #Puts it in a global variable
                root.title(file_open_name[0]+' - ' + name) #Puts the name of the file in the window's title
                break

    def f_help():
        os.system("start \"\" http:\\christopher-hatton.co.uk")

    #Configure grid:
    Grid.rowconfigure(root,index = 2,weight = 4)
    Grid.columnconfigure(root,index = 0,weight = 1)

    #Make Tk:
    heading = Label(text = name,font = 'Helvetica 30 bold')
    textbox = scrolledtext.ScrolledText(width=40, height=10)
    frame_buttons = tk.Frame(root)
    open_file = Button(frame_buttons,text = 'Open',command = f_open_file)
    open_file.pack(side=tk.LEFT,padx=(3))
    save_file = Button(frame_buttons,text = 'Save',command=lambda : f_save_file())
    save_file.pack(side=tk.LEFT,padx=(3))
    save_as = Button(frame_buttons,text = 'Save As',command=lambda : f_save_as())
    save_as.pack(side=tk.LEFT,padx=(3))
    help_button = Button(frame_buttons,text = 'Help',command = f_help)
    help_button.pack(side=tk.LEFT,padx=(3))
    copyright = Label(text = '© 2021 - Christopher Hatton (558) - Christopher@Christopher-Hatton.co.uk')

    #Arrange Tk:
    heading.grid(row = 0,column = 0,sticky = 'nsew')
    frame_buttons.grid(row = 1,column = 0)
    textbox.grid(row = 2,column = 0,sticky = 'nsew')
    copyright.grid(row = 3,column = 0,sticky = 'nsew')

    #Keybinds:
    root.bind('<Control-s>', f_save_file_key)
    root.bind('<Control-o>', f_open_file_key)
    root.bind('<F12>', f_save_as_key)

    root.mainloop()
     
def small_monitor(): #displays error message for small screen
    root = Tk()
    warning_label = Label(text = 'Your screen is too small')
    warning_label.grid(row = 0,column = 0)
    root.mainloop

def f_linux():
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Linux version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop  

def f_mac():
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Mac version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop  

def f_unknown_os():
    root = Tk()
    warning_label = Label(text = name + ' is not available for your operating system.')
    warning_label.grid(row = 0,column = 0)
    root.mainloop      

def run(): #if screen size big enough, run
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    if width >= 1280 and height >= 720:
        f_main()
    else:
        small_monitor()

if platform == 'win32': #if os = win32, run
    run()
elif platform == 'linux' or platform == 'linux32':
    f_linux() #if os = linux, asks the user to get the linux version
elif platform == 'darwin':
    f_mac() #if os = osx, asks the user to get the osx version
else:
    f_unknown_os() #for unknown os