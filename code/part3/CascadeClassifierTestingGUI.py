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
import generate_code

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
    playlistbox.insert(index, filename_path)
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

scrollbar1 = Scrollbar(leftframe, orient=HORIZONTAL)
scrollbar1.pack( side = BOTTOM, fill = X )

playlistbox = Listbox(leftframe, width=50,height=30, xscrollcommand = scrollbar1.set, yscrollcommand = scrollbar.set)
playlistbox.pack()

scrollbar1.config( command = playlistbox.xview )
scrollbar.config( command = playlistbox.yview )

addBtn = ttk.Button(leftframe, text="Add Cascade", command=browse_file)
addBtn.pack(side=LEFT)


def del_config():
    selected_cascade = playlistbox.curselection()
    selected_cascade = int(selected_cascade[0])
    #playlistbox.delete(0,END)
    playlistbox.delete(selected_cascade)
    playlist.pop(selected_cascade)


delBtn = ttk.Button(leftframe, text="Delete selected Cascade", command=del_config)
delBtn.pack(side=LEFT)

scaleFactor_text=""
cascade_text=""
def message_scale_factor():
    global scaleFactor_text,cascade_text,selected_conf
    scaleFactor_text=simpledialog.askstring(title="scaleFactor", prompt="scaleFactor example: 1:10")
    print(scaleFactor_text)
    splited_text=cascade_text.split()
    print(splited_text)
    splited_text=splited_text[:1]+splited_text[2:]
    splited_text.insert(1,scaleFactor_text)
    cascade_text=' '.join(splited_text)
    #cascade_text+=" "+scaleFactor_text
    print(cascade_text,"cascade_text")
    print(playlistbox.index(selected_conf),"printing selected_conf from playlist")
    playlistbox.delete(selected_conf)
    playlist.pop(selected_conf)
    playlistbox.insert(selected_conf,cascade_text)
    playlist.insert(selected_conf,cascade_text)
minNeighbours_text=""
def min_neighbours_factor():
    global minNeighbours_text,cascade_text,selected_conf
    minNeighbours_text=simpledialog.askstring(title="minNeighbours", prompt="minNeighbours example: 5")
    print(minNeighbours_text)
    splited_text=cascade_text.split()
    splited_text=splited_text[:2]
    splited_text.insert(2,minNeighbours_text)
    cascade_text=' '.join(splited_text)
    print(cascade_text,"cascade_text")
    print(playlistbox.index(selected_conf),"printing selected_conf from playlist")
    playlistbox.delete(selected_conf)
    playlist.pop(selected_conf)
    playlistbox.insert(selected_conf,cascade_text)
    playlist.insert(selected_conf,cascade_text)

first_t1=0
first_t2=0
scaleFactor=""
minNeighbours=""
selected_conf=0
def edit_config():
    global first_t1,scaleFactor,scaleFactor_text,minNeighbours_text,first_t2,cascade_text,minNeighbours,selected_conf
    #this section is in middle right frame
    selected_conf = playlistbox.curselection()
    selected_conf = int(selected_conf[0])
    #playlistbox.delete(0,END)
    #selected song is just the index from list
    print("printing selected song",selected_conf)
    #print(playlist[selected_song])
    cascade_text=playlist[selected_conf]
    if first_t1!=0:
        scaleFactor.destroy()
        scaleFactor = ttk.Button(middleframe, text="Edit scaleFactor", command=message_scale_factor)
        scaleFactor.pack(side=LEFT)
    else:
        scaleFactor = ttk.Button(middleframe, text="Edit scaleFactor", command=message_scale_factor)
        scaleFactor.pack(side=LEFT)
        first_t1=1
    if first_t2!=0:
        minNeighbours.destroy()
        minNeighbours = ttk.Button(middleframe, text="Edit minNeighbours", command=min_neighbours_factor)
        minNeighbours.pack(side=LEFT)
    else:
        minNeighbours = ttk.Button(middleframe, text="Edit minNeighbours", command=min_neighbours_factor)
        minNeighbours.pack(side=LEFT)
        first_t2=1


#here starts right frame

image_path=""
first_t=0
image_path_label=""
def browse_img():
    global image_path,first_t,image_path_label
    image_path = filedialog.askopenfilename()
    print(image_path,"image path")
    if first_t!=0:
        image_path_label.destroy()
        image_path_label = ttk.Label(topframe, text=image_path, relief=GROOVE)
        image_path_label.pack(padx=15,pady=7)
    else:
        image_path_label = ttk.Label(topframe, text=image_path, relief=GROOVE)
        image_path_label.pack(padx=15,pady=7)
        first_t=1


cascade_path=""
cascade_t=0
cascade_path_label=""
def browse_cascade():
    global cascade_path,cascade_t,cascade_path_label
    cascade_path = filedialog.askopenfilename()
    print(cascade_path,"image path")
    if cascade_t!=0:
        cascade_path_label.destroy()
        cascade_path_label = ttk.Label(topframe1, text=cascade_path, relief=GROOVE)
        cascade_path_label.pack(padx=15,pady=7)
    else:
        cascade_path_label = ttk.Label(topframe1, text=cascade_path, relief=GROOVE)
        cascade_path_label.pack(padx=15,pady=7)
        cascade_t=1

rightframe = Frame(root)
rightframe.pack(pady=15)

#top right
topframe = Frame(rightframe)
topframe.pack()

delBtn = ttk.Button(topframe, text="Browse Image", command=browse_img)
delBtn.pack(side=LEFT)

topframe1 = Frame(rightframe)
topframe1.pack(pady=10)

delBtn2 = ttk.Button(topframe1, text="Browse Config", command=browse_cascade)
delBtn2.pack(side=LEFT)
# info_label = ttk.Label(topframe1, text="select Cascade and edit following values", relief=GROOVE)
# info_label.pack(padx=25, pady=25)

#middle right
middleframe = Frame(rightframe)
middleframe.pack(pady=25, padx=25)

delBtn = ttk.Button(middleframe, text="Edit cascade", command=edit_config)
delBtn.pack(side=LEFT)


#bottom right
#actually cascade_path is the path to the configuration file
def process_config():
    global cascade_path,image_path
    if cascade_path!="" and image_path!="":
        generate_code.Generate(cascade_path,image_path)
bottomframe = Frame(rightframe)
bottomframe.pack()

delBtn = ttk.Button(bottomframe, text="Generate Program", command=process_config)
delBtn.pack(side=LEFT)

#bottom most frame

program_path=r""
cascade_tp=0
program_path_label=""
def browse_program():
    global program_path,cascade_tp,program_path_label
    program_path = filedialog.askopenfilename()
    print(program_path,"program path")
    if cascade_tp!=0:
        program_path_label.destroy()
        program_path_label = ttk.Label(bottom_mostframe, text=program_path, relief=GROOVE)
        program_path_label.pack(padx=15,pady=7)
    else:
        program_path_label = ttk.Label(bottom_mostframe, text=program_path, relief=GROOVE)
        program_path_label.pack(padx=15,pady=7)
        cascade_tp=1

def run_program():
    global program_path
    #norm_path = os.path.normpath(program_path)
    os.system("python {}".format(program_path))

bottom_mostframe = Frame(rightframe)
bottom_mostframe.pack(pady=25, padx=25)

delBtnB = ttk.Button(bottom_mostframe, text="Browse Program", command=browse_program)
delBtnB.pack(side=LEFT)

bottom_mostframe1 = Frame(rightframe)
bottom_mostframe1.pack(pady=25, padx=25)

delBtnb1 = ttk.Button(bottom_mostframe1, text="Run Program", command=run_program)
delBtnb1.pack(side=LEFT,pady=20)

def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
