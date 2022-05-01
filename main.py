import tkinter as tk
from tkinter import filedialog as fd
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import algorithm

# Created by Vishal Dillibabu, Shyan Vilvarajah and Rabten Tsering.

#Back button
def back(window,samewindow):
    samewindow.destroy()
    window.deiconify()

#Encryption
def select_file_en():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Pick File',
        initialdir='/',
        filetypes=filetypes)
    filenames = str(filename).split("/")
    file = filenames[-1]
    if algorithm.encrypt_checker(file):
        print(algorithm.encrypt(file))
        showinfo(title="Sucess", message ="File has been sucessfully encrypted! key for file is in console please save it")
    else:
        showinfo(title="ERROR!",message="File has already been encrypted!")


def encrypter_create(withdrawed_window):
    window = tk.Tk()
    window.title("Encrypter")
    window.geometry("400x300")
    withdrawed_window.withdraw()
    select = tk.Button(window,text="Select File",command=select_file_en)
    select.place(x=140,y=100)

    back_button = tk.Button(window,text="Previous Page",command= lambda: back(withdrawed_window,window))
    back_button.place(x = 0, y = 0)


#Decryption
def select_file_de():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Pick File',
        initialdir='/',
        filetypes=filetypes)
    filenames = str(filename).split("/")
    print(filenames)
    file = filenames[-1]
    print(file)
    if algorithm.encrypt_checker(file):
        showinfo(title="ERROR!",message="File hasn't been encrypted yet!")
    else:
        key = askstring("Key","Enter key given when you encrypted the file here: ")
        key_dict = algorithm.decrypt_checker()
        if key_dict[file] == key:
            algorithm.decrypt(file)
            showinfo(title="Sucess", message= "File has been decrypted sucessfully!")
        else:
            showinfo(title="ERROR!",message="Incorrect key for the file")


def decrypter_create(withdrawed_window):
    window = tk.Tk()
    window.title("Decrypter")
    window.geometry("400x300")
    withdrawed_window.withdraw()
    select = tk.Button(window,text="Select File",command=select_file_de)
    select.place(x=140,y=100)

    back_button = tk.Button(window,text="Previous Page",command= lambda: back(withdrawed_window,window))
    back_button.place(x = 0, y = 0)


if __name__ == "__main__":
    first_window = tk.Tk()
    first_window.title("Encrypt-Decrypt")
    first_window.geometry("400x100")
    encrypt_button = tk.Button(first_window, text="ENCRYPT", height=2,width=10, command= lambda: encrypter_create(first_window))
    encrypt_button.place(x=60,y=25)
    decrypt_button = tk.Button(first_window, text="DECRYPT", height=2,width=10,command=lambda: decrypter_create(first_window))
    decrypt_button.place(x=220,y=25)

    # password = algorithm.encrypt(file)
    # algorithm.encrypt("keys and file names.txt")
    # print(f"File Successfully Encrypted. The password for this encrypted file is {password},          please save it. ")



tk.mainloop()
