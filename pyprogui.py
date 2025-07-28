from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from pathlib import Path


def gui():
    global root
    root = Tk()
    root.title("GUI CRUD")
    root.geometry("1000x500")
    
    
def file():
    global teks_file
    teks_file = tk.StringVar()
    file_label = tk.Label(root, text = "Nama File: ", font = ('calibre', 10, 'normal'))
    file_label.place(x = 40, y = 30)
    file_entry = tk.Entry(root, textvariable = teks_file, font = ('calibre', 10, 'normal'))
    file_entry.place(x = 115, y = 30)
    
def teks():
    global teks_entry
    teks_label = tk.Label(root, text = "Teks: ", font = ('calibre', 10, 'normal'))
    teks_label.place(x = 40, y = 80)
    teks_entry = tk.Text(root, width = 50 ,height = 8, font = ('calibre', 10, 'normal'))
    teks_entry.place(x = 40, y = 110)
      
def buatFile():
    input_file = teks_file.get()
    input_teks = teks_entry.get('1.0', tk.END)
    if not input_file.endswith(".txt"):
        input_file += '.txt'
    with open(input_file, 'w', encoding = 'utf-8') as file:
        file.write(input_teks)
    teks_entry.delete("1.0", tk.END)
    showTeks()
    
        
def button_create():
    create = Button(root, text = "Create", command = buatFile)
    create.place(x = 415, y = 140)
    
def appendFile():
    input_file = teks_file.get()
    input_teks = teks_entry.get('1.0', tk.END)
    if not input_file.endswith(".txt"):
            input_file += '.txt'
    with open(input_file, 'a', encoding = 'utf-8') as file:
        file.write(input_teks)
    teks_entry.delete("1.0", tk.END)
    showTeks()
        
def button_append():
    append = Button(root, text = "Append", command = appendFile)
    append.place(x = 415, y = 170)
    
def showTampil():
    global tampil_entry
    tampil_label = tk.Label(root, text = "Tampil: ", font = ('calibre', 10, 'normal'))
    tampil_label.place(x = 525, y = 80)
    tampil_entry = tk.Text(root, width = 50 ,height = 8, font = ('calibre', 10, 'normal'))
    tampil_entry.place(x = 525, y = 110)
    
    
def showTeks():
    input_file = teks_file.get()
    if not input_file.endswith(".txt"):
            input_file += '.txt'
    with open(input_file, 'r', encoding = 'utf-8') as file:
        isiFile = file.read()
        tampil_entry.delete('1.0', tk.END)
        tampil_entry.insert(tk.END, isiFile)
        
def Read():
    input_file = teks_file.get()
    if not input_file.endswith(".txt"):
            input_file += '.txt'
    with open(input_file, 'r', encoding = 'utf-8') as file:
        isiFile = file.read()
        tampil_entry.delete('1.0', tk.END)
        tampil_entry.insert(tk.END, isiFile)
        
def buttonRead():
    read = Button(root, text = "Read", command = Read)
    read.place(x = 900, y = 150)
        
def search():
    global teks_search
    teks_search = tk.StringVar()
    search_label = tk.Label(root, text = "Search Text: ", font = ('calibre', 10, 'normal'))
    search_label.place(x = 40, y = 265)
    search_entry = tk.Entry(root, textvariable = teks_search, font = ('calibre', 10, 'normal'))
    search_entry.place(x = 40, y = 290)
    
def update():
    global teks_update
    teks_update = tk.StringVar()
    update_label = tk.Label(root, text = "Update Text: ", font = ('calibre', 10, 'normal'))
    update_label.place(x = 220, y = 265)
    update_entry = tk.Entry(root, textvariable = teks_update, font = ('calibre', 10, 'normal'))
    update_entry.place(x = 220, y = 290)
    
def updateData():
    cariKata = teks_search.get()
    kataBaru = teks_update.get()
    input_file = teks_file.get()
    if not input_file.endswith(".txt"):
            input_file += '.txt'
    with open(input_file, 'r', encoding = 'utf-8') as file:
        isiFile = file.read()
        if cariKata in isiFile:
            ganti = isiFile.replace(cariKata, kataBaru)
    with open(input_file, 'w', encoding = 'utf-8') as file:
        file.write(ganti)
    Read()
    
def buttonUpdate():
    update = Button(root, text = "Update", command = updateData)
    update.place(x = 380, y = 285)
    
def hapus():
    global teks_hapus
    teks_hapus = tk.StringVar()
    hapus_label = tk.Label(root, text = "File: ", font = ('calibre', 10, 'normal'))
    hapus_label.place(x = 40, y = 350)
    hapus_entry = tk.Entry(root, textvariable = teks_hapus, font = ('calibre', 10, 'normal'))
    hapus_entry.place(x = 40, y = 375)    
    
def hapusFile():
    input_hapus = teks_hapus.get()
    if not input_hapus.endswith(".txt"):
        input_hapus += '.txt'
        file_path = Path(input_hapus)
    file_path.unlink()
    tampil_entry.delete("1.0", tk.END)
def buttonHapus():
    update = Button(root, text = "Delete", command = hapusFile)
    update.place(x = 40, y = 400)    

    

gui()
file()
teks()
button_create()
button_append()
showTampil()
buttonRead()
search()
update()
buttonUpdate()
hapus()
buttonHapus()
root.mainloop()