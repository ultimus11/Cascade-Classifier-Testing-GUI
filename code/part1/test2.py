import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk
from ttkthemes import themed_tk as tk
import random

root = tk.ThemedTk()
root.get_themes()                 # Returns a list of all themes that can be set
root.set_theme("radiance")         # Sets an available theme

# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
#
# Styles - normal, bold, roman, italic, underline, and overstrike.


statusbar = ttk.Label(root, text="Welcome to Cascade Tester", relief=SUNKEN, anchor=W, font='Times 10 italic')
statusbar.pack(side=BOTTOM, fill=X)

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)

playlist = []


def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)


def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    #filenamepath is entire path like cascades/wow/new/ok.cascade
    #filename is just last name in path which is like ok.cascade
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)

def browse_playlist():
    print("browsing cascades")
    global filename_path
    print("loding cascades")
    playlistbox.delete(0,END)
    playlist.clear()
    print(playlist)
    listnameinp=filedialog.askopenfilename()
    listnameinp = os.path.basename(listnameinp)
    f_name=open(listnameinp, "r", encoding='UTF8')
    slength=len(f_name.read().splitlines())
    f_name.close()
    jj=0
    f_name=open(listnameinp, "r", encoding='UTF8')
    while jj < slength:
        filename_path=f_name.readline().rstrip()
        print("printing file path here")
        print(filename_path)
        jj+=1
        add_to_playlist(filename_path)
    f_name.close()
def save_playlist():
    print("saving playlist")
    userinp=simpledialog.askstring(title="Save Configuration", prompt="Name for your Configuration")
    songlist=playlistbox.get(0,END)
    userinp=userinp+".config"
    playlistsave = open(userinp, "w", encoding='UTF8')
    for xx in playlist:
        print(xx)
        playlistsave.write(xx)
        playlistsave.write("\n")
    playlistsave.close()

def load_playlist():
    global filename_path
    print("loding playlists")
    playlistbox.delete(0,END)
    playlist.clear()
    print(playlist)
    listnameinp=simpledialog.askstring(title="Load Configuration", prompt="Name of your Configuration")
    listnameinp=listnameinp+".config"
    f_name=open(listnameinp, "r", encoding='UTF8')
    slength=len(f_name.read().splitlines())
    f_name.close()
    jj=0
    f_name=open(listnameinp, "r", encoding='UTF8')
    while jj < slength:
        filename_path=f_name.readline().rstrip()
        print("printing file path here")
        print(filename_path)
        jj+=1
        add_to_playlist(filename_path)
    f_name.close()

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Configuration", menu=subMenu)
subMenu.add_command(label="Save config", command=save_playlist)
subMenu.add_command(label="Load config", command=load_playlist)
subMenu.add_command(label="Browse config", command=browse_playlist)



def about_us():
    tkinter.messagebox.showinfo('About GUI', 'This is the GUI software for generating Object detection python program\nYou can also run the generated program anywhere')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)


root.title("Auto Cascade Tester")
#root.iconbitmap(r'images/testergui.ico')

# Root Window - StatusBar, LeftFrame, RightFrame
# LeftFrame - The listbox (playlist)
# RightFrame - TopFrame,MiddleFrame and the BottomFrame

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

scrollbar = Scrollbar(leftframe)
scrollbar.pack( side = RIGHT, fill = Y )

playlistbox = Listbox(leftframe, yscrollcommand = scrollbar.set)
playlistbox.pack()

scrollbar.config( command = playlistbox.yview )
addBtn = ttk.Button(leftframe, text="Add Cascade", command=browse_file)
addBtn.pack(side=LEFT)


def del_config():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    #playlistbox.delete(0,END)
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


delBtn = ttk.Button(leftframe, text="Delete selected Cascade", command=del_config)
delBtn.pack(side=LEFT)

def edit_config():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    #playlistbox.delete(0,END)
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)





#here starts right frame

rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Configure Cascade')
lengthlabel.pack(pady=15)

currenttimelabel = ttk.Label(topframe, text='Select Cascade then update the following values', relief=GROOVE)
currenttimelabel.pack()

middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)

bottomframe = Frame(rightframe)
bottomframe.pack()

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
