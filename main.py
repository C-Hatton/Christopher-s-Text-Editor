#Made by Christopher Hatton (558)

# -*-coding: utf-8-*-

from tkinter import *            #for Tk window
import tkinter as tk             #to make Frame
from tkinter import scrolledtext #to create textbox
from tkinter import filedialog   #to open and choose documents
from sys import platform         #to make sure that the os is win32
import ctypes                    #to make sure that the screen size is large enough
import time                      #to make better timings
import os                        #to allow help button open help web page
import importlib                 #to open custom theme
 
name = "Christopher's Text Editor"

def f_main():

    f = open('theme.txt','r')
    theme = f.read()
    f.close()

    f_theme = importlib.import_module(theme)

    #START:
    root = tk.Tk()
                           
    root.iconphoto(True, tk.PhotoImage(file='logo.ico'))                                                  #Changes icon
    root.state('zoomed')                                                                                  #Sets default state to zoomed
    root.bind('<F11>', lambda event: root.attributes('-fullscreen',not root.attributes('-fullscreen')))   #Binds F11 to fullscreen
    root.bind('<Escape>', lambda event: root.attributes('-fullscreen', False))                            #Binds Escape to leave fullscreen
    root.bind('<F10>', lambda event: root.state('zoomed'))                                                #Binds F10 to zoomed    
    root.title(name)                                                                                      #Sets the title of the window

    #Make global variables:
    file_location_save = ['']
    file_open = [False]
    file_open_name = ['']
    font_size,font_style,font_type,text_colour,button_fg,button_bg,heading_fg,heading_bg,text_box_colour = f_theme.f_themes()
    font_style_all = font_type + ' ' + font_size + ' ' + font_style

    def f_open_file(): #Open files:
        file_location = ''
        file_location = filedialog.askopenfilename() #Gets the file location (local variable)
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
        file_location = filedialog.askopenfilename() #Gets the file location (local variable)
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
            file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
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
                file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
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
        file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
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
        file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
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
   
    def f_replace_text(original_text,replace_text): #Replaces text

        x = textbox.get("1.0",'end-1c')
        y = x.replace(original_text, replace_text)
        textbox.delete("1.0","end")
        textbox.insert("end-1c",y) #Puts the contents of the file in the textbox

    def f_replace(): #Replace text

        def f_submit():
            original_text = original.get() #Gets inputs
            replace_text = replace.get()
            f_replace_text(original_text,replace_text)
            popup.destroy()

        def f_submit_key(event):
            original_text = original.get() #Gets inputs
            replace_text = replace.get()
            f_replace_text(original_text,replace_text)
            popup.destroy()

        popup = Toplevel(root) #Creates a popup
        popup.title('Replace Text - ' + name)
        original_label = Label(popup, text = 'What do you want to replace?')
        replace_label = Label(popup,text = 'What do you want to replace it with?')
        original = Entry(popup)
        replace = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        original_label.grid(row = 0,column = 0)
        replace_label.grid(row = 0,column = 2)
        original.grid(row = 1,column = 0)
        replace.grid(row = 1,column = 2)
        submit.grid(row = 2,column = 1,pady = 3)
        popup.bind('<Return>',f_submit_key)

    def f_replace_key(event): #Replace text

        def f_submit():
            original_text = original.get() #Gets inputs
            replace_text = replace.get()
            f_replace_text(original_text,replace_text)
            time.sleep(0.5)
            popup.destroy()

        def f_submit_key(event):
            original_text = original.get() #Gets inputs
            replace_text = replace.get()
            f_replace_text(original_text,replace_text)
            popup.destroy()

        popup = Toplevel(root) #Creates a popup
        popup.title('Replace Text - ' + name)
        original_label = Label(popup, text = 'What do you want to replace?')
        replace_label = Label(popup,text = 'What do you want to replace it with?')
        original = Entry(popup)
        replace = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        original_label.grid(row = 0,column = 0)
        replace_label.grid(row = 0,column = 2)
        original.grid(row = 1,column = 0)
        replace.grid(row = 1,column = 2)
        submit.grid(row = 2,column = 1,pady = 3)
        popup.bind('<Return>',f_submit_key)

    def f_change_text_style(): #Changes font style of textbox

        def f_submit():
            text_style = text_style_entry.get()    
            textbox.configure(font=(text_style))
            time.sleep(0.5)
            popup.destroy()
            if text_style.split()[0] == 'Courier' or text_style.split()[0] == 'Helvetica' or text_style.split()[0] == 'Times':
                f = open('font_type.txt','w')
                f.write(text_style.split()[0])
                f.close()
            f = open('font_size.txt','r')
            x = f.read()
            f.close()
            z = 0
            f = open('font_size.txt','w')
            while True:
                try:
                    f.write(text_style.split()[1])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_size.txt','w')
                f.write(text_style.split()[1])
                f.close()
                z = z - 1
            f = open('font_size.txt','r')
            y = f.read()
            f.close()
            f = open('font_style.txt','w')
            while True:
                try:
                    f.write(text_style.split()[2])
                except IndexError:
                    break
                else:
                    z = z + 1
                    break
            f.close()
            if z == 1:
                f = open('font_style.txt','w')
                f.write(text_style.split()[2])
                f.close()
                z = z - 1

        def f_submit_key(event):
            text_style = text_style_entry.get()    
            textbox.configure(font=(text_style))
            time.sleep(0.5)
            popup.destroy()
            if text_style.split()[0] == 'Courier' or text_style.split()[0] == 'Helvetica' or text_style.split()[0] == 'Times':
                f = open('font_type.txt','w')
                f.write(text_style.split()[0])
                f.close()
            f = open('font_size.txt','r')
            x = f.read()
            f.close()
            z = 0
            f = open('font_size.txt','w')
            while True:
                try:
                    f.write(text_style.split()[1])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_size.txt','w')
                f.write(text_style.split()[1])
                f.close()
                z = z - 1
            f = open('font_size.txt','r')
            y = f.read()
            f.close()
            f = open('font_style.txt','w')
            while True:
                try:
                    f.write(text_style.split()[2])
                except IndexError:
                    break
                else:
                    z = z + 1
                    break
            f.close()
            if z == 1:
                f = open('font_style.txt','w')
                f.write(text_style.split()[2])
                f.close()
                z = z - 1

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        text_style_label = Label(popup, text = 'Enter text style here:')
        text_style_entry = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        text_style_label.grid(row = 0,column = 0)
        text_style_entry.grid(row = 1,column = 0,padx = 5)
        submit.grid(row = 2,column = 0,pady = 3)
        popup.bind('<Return>',f_submit_key)

    def f_change_text_style_key(event): #Changes font style of textbox

        def f_submit():
            text_style = text_style_entry.get()    
            textbox.configure(font=(text_style))
            time.sleep(0.5)
            popup.destroy()
            if text_style.split()[0] == 'Courier' or text_style.split()[0] == 'Helvetica' or text_style.split()[0] == 'Times':
                f = open('font_type.txt','w')
                f.write(text_style.split()[0])
                f.close()
            f = open('font_size.txt','r')
            x = f.read()
            f.close()
            z = 0
            f = open('font_size.txt','w')
            while True:
                try:
                    f.write(text_style.split()[1])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_size.txt','w')
                f.write(x)
                f.close()
                z = z - 1
            f = open('font_style.txt','r')
            y = f.read()
            f.close()
            f = open('font_style.txt','w')
            while True:
                try:
                    f.write(text_style.split()[2])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_style.txt','w')
                f.write(y)
                f.close()
                z = z - 1

        def f_submit_key(event):
            text_style = text_style_entry.get()    
            textbox.configure(font=(text_style))
            time.sleep(0.5)
            popup.destroy()
            if text_style.split()[0] == 'Courier' or text_style.split()[0] == 'Helvetica' or text_style.split()[0] == 'Times':
                f = open('font_type.txt','w')
                f.write(text_style.split()[0])
                f.close()
            f = open('font_size.txt','r')
            x = f.read()
            f.close()
            z = 0
            f = open('font_size.txt','w')
            while True:
                try:
                    f.write(text_style.split()[1])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_size.txt','w')
                f.write(x)
                f.close()
                z = z - 1
            f = open('font_style.txt','r')
            y = f.read()
            f.close()
            f = open('font_style.txt','w')
            while True:
                try:
                    f.write(text_style.split()[2])
                except IndexError:
                    z = z + 1
                    break
                else:
                    break
            f.close()
            if z == 1:
                f = open('font_style.txt','w')
                f.write(y)
                f.close()
                z = z - 1

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        text_style_label = Label(popup, text = 'Enter text style here:')
        text_style_entry = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        text_style_label.grid(row = 0,column = 0)
        text_style_entry.grid(row = 1,column = 0,padx = 5)
        submit.grid(row = 2,column = 0,pady = 3)
        popup.bind('<Return>',f_submit_key)

    def f_change_text_colour():

        def f_submit():
           
            colour = text_colour_entry.get()
            textbox.configure(fg = colour)
            time.sleep(0.5)
            popup.destroy()
            if not colour:
                raise SystemExit
            else:
                f = open('text_colour.txt','w')
                f.write(colour)
                f.close()

        def f_submit_key(event):
           
            colour = text_colour_entry.get()
            textbox.configure(fg = colour)
            time.sleep(0.5)
            popup.destroy()
            if not colour:
                raise SystemExit
            else:
                f = open('text_colour.txt','w')
                f.write(colour)
                f.close()

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        text_colour_label = Label(popup, text = 'Enter text colour here:')
        text_colour_entry = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        text_colour_label.grid(row = 0,column = 0)
        text_colour_entry.grid(row = 1,column = 0,padx = 5)
        submit.grid(row = 2,column = 0,pady = 3)
        popup.bind('<Return>',f_submit_key)

    def f_change_text_colour_key(event):

        def f_submit():
           
            colour = text_colour_entry.get()
            textbox.configure(fg = colour)
            popup.destroy()
            if not colour:
                raise SystemExit
            else:
                f = open('text_colour.txt','w')
                f.write(colour)
                f.close()

        def f_submit_key(event):
           
            colour = text_colour_entry.get()
            textbox.configure(fg = colour)
            popup.destroy()
            if not colour:
                raise SystemExit
            else:
                f = open('text_colour.txt','w')
                f.write(colour)
                f.close()

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        text_colour_label = Label(popup, text = 'Enter text colour here:')
        text_colour_entry = Entry(popup)
        submit = Button(popup,text = 'Submit',command = f_submit,bg = button_bg,fg = button_fg)
        text_colour_label.grid(row = 0,column = 0)
        text_colour_entry.grid(row = 1,column = 0,padx = 5)
        submit.grid(row = 2,column = 0,pady = 3)
        popup.bind('<Return>',f_submit_key)
   
    def f_themes(): #Set themes

        def f_get_themes():
            os.system('start \"\" https://github.com/C-Hatton/Christopher-s-Text-Editor')
            popup.destroy()

        def f_open_themes():
            file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
            x = file_location.split('/') #Gets the name of the file(local variable)
            if not x:
                raise SystemExit
            else:
                y = (x[-1].split('.'))[0]
                f = open('theme.txt','w')
                f.write(y)
                f.close()
            popup.destroy()

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        label_1 = Label(popup,text = 'Download themes here:')
        label_1.grid(row = 0,column = 0,pady = 3,padx = 3)
        button_1 = Button(popup,text = 'Link to themes',command = f_get_themes,bg = button_bg,fg = button_fg)
        button_1.grid(row = 1,column = 0,pady = 3,padx = 3)
        label_2 = Label(popup,text = 'Choose theme:')
        label_2.grid(row = 2,column = 0,pady = 3,padx = 3)
        button_2 = Button(popup,text = 'Choose theme',command = f_open_themes,bg = button_bg,fg = button_fg)
        button_2.grid(row = 3,column = 0,pady = 3,padx = 3)

    def f_themes_key(event): #Set themes

        def f_get_themes():
            os.system('start \"\" https://github.com/C-Hatton/Christopher-s-Text-Editor')
            popup.destroy()

        def f_open_themes():
            file_location = filedialog.askopenfilename() #Gets the file to save to (local variable)
            x = file_location.split('/') #Gets the name of the file(local variable)
            if not x:
                raise SystemExit
            else:
                y = (x[-1].split('.'))[0]
                f = open('theme.txt','w')
                f.write(y)
                f.close()
            popup.destroy()

        popup = Toplevel(root) #Creates a popup
        popup.title('Change Text Style - ' + name)
        label_1 = Label(popup,text = 'Download themes here:')
        label_1.grid(row = 0,column = 0,pady = 3,padx = 3)
        button_1 = Button(popup,text = 'Link to themes',command = f_get_themes,bg = button_bg,fg = button_fg)
        button_1.grid(row = 1,column = 0,pady = 3,padx = 3)
        label_2 = Label(popup,text = 'Choose theme:')
        label_2.grid(row = 2,column = 0,pady = 3,padx = 3)
        button_2 = Button(popup,text = 'Choose theme',command = f_open_themes,bg = button_bg,fg = button_fg)
        button_2.grid(row = 3,column = 0,pady = 3,padx = 3)

    def f_help():
        os.system('start \"\" https://github.com/C-Hatton/Christopher-s-Text-Editor')

    #Configure grid:
    Grid.rowconfigure(root,index = 2,weight = 4)
    Grid.columnconfigure(root,index = 0,weight = 1)

    #Make Tk:
    heading = Label(root,text = name,font = 'Helvetica 25 bold',bg = heading_bg,fg = heading_fg)
    textbox = scrolledtext.ScrolledText(width=40, height=10,bg = text_box_colour)
    frame_buttons = tk.Frame(root,bg = heading_bg)
    br1 = Button(frame_buttons,bg = heading_bg,borderwidth=0)
    br1.pack(side=tk.LEFT,padx=(3),pady=(3),expand=YES)
    open_file = Button(frame_buttons,text = 'Open',command = f_open_file,bg = button_bg,fg = button_fg)
    open_file.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    save_file = Button(frame_buttons,text = 'Save',command=lambda : f_save_file(),bg = button_bg,fg = button_fg)
    save_file.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    save_as = Button(frame_buttons,text = 'Save As',command=lambda : f_save_as(),bg = button_bg,fg = button_fg)
    save_as.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    replace_button = Button(frame_buttons,text = 'Replace Text',command=lambda : f_replace(),bg = button_bg,fg = button_fg)
    replace_button.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    change_text_style = Button(frame_buttons,text = 'Change Text Style',command=lambda : f_change_text_style(),bg = button_bg,fg = button_fg)
    change_text_style.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    change_text_colour = Button(frame_buttons,text = 'Change Text Colour',command=lambda : f_change_text_colour(),bg = button_bg,fg = button_fg)
    change_text_colour.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    themes = Button(frame_buttons,text = 'Themes',command=lambda : f_themes(),bg = button_bg,fg = button_fg)
    themes.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    help_button = Button(frame_buttons,text = 'Help',command = f_help,bg = button_bg,fg = button_fg)
    help_button.pack(side=tk.LEFT,padx=(3),pady=(3),expand=NO)
    br2 = Button(frame_buttons,bg = heading_bg,borderwidth=0)
    br2.pack(side=tk.LEFT,padx=(3),pady=(3),expand=YES)
    copyright = Label(root,text = '© 2021 - Christopher Hatton (558) - Christopher@Christopher-Hatton.co.uk',bg = heading_bg,fg = heading_fg)

    #Configure textbox:
    textbox.configure(font = font_style_all,fg = text_colour)

    #Arrange Tk:
    heading.grid(row = 0,column = 0,sticky = 'nsew')
    frame_buttons.grid(row = 1,column = 0,sticky = 'nsew')
    textbox.grid(row = 2,column = 0,sticky = 'nsew')
    copyright.grid(row = 3,column = 0,sticky = 'nsew')

    #Keybinds:
    root.bind('<Control-s>', f_save_file_key)
    root.bind('<Control-o>', f_open_file_key)
    root.bind('<F12>', f_save_as_key)
    root.bind('<Control-h>', f_replace_key)
    root.bind('<Control-f>', f_change_text_style_key)
    root.bind('<Control-b>', f_change_text_colour_key)
    root.bind('<Control-t>', f_themes_key)

    root.mainloop()
     
def small_monitor(): #displays error message for small screen
    root = Tk()
    warning_label = Label(text = 'Your screen is too small')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()

def f_linux(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Linux version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()  

def f_mac(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Mac version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()  

def f_unknown_os(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = name + ' is not available for your operating system.')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()      

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
