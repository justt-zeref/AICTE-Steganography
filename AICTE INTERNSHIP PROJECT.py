from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('700x480')
win.config(bg='black')

# Global password variable
user_password = "1234"  # Default password
password_file = "password.txt"

def load_password():
    global user_password
    if os.path.exists(password_file):
        with open(password_file, "r") as file:
            user_password = file.read().strip()

def save_password(new_password):
    global user_password
    user_password = new_password
    with open(password_file, "w") as file:
        file.write(new_password)

def set_password():
    """Allow user to change the password."""
    new_password = password_entry.get()
    
    if new_password:
        save_password(new_password)
        messagebox.showinfo("Success", "Password changed successfully!")
        password_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Password cannot be empty!")

def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'),
                                                      ('All file', '*.*')))
    if open_file:
        img = Image.open(open_file)
        img = img.resize((250, 220), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        lf1.config(image=img)
        lf1.image = img

def hide():
    global hide_msg
    password = code.get()
    if password == user_password:
        msg = text1.get(1.0, END).strip()
        if open_file and msg:
            hide_msg = lsb.hide(open_file, msg)
            messagebox.showinfo('Success', 'Message successfully hidden in the image. Please save your image.')
        else:
            messagebox.showerror('Error', 'Please select an image and enter a message.')
    else:
        messagebox.showerror('Error', 'Incorrect Secret Key')

def save_img():
    if 'hide_msg' in globals():
        save_path = filedialog.asksaveasfilename(defaultextension='.png',
                                                 filetypes=[("PNG file", "*.png")])
        if save_path:
            hide_msg.save(save_path)
            messagebox.showinfo('Saved', f'Image successfully saved at {save_path}')
    else:
        messagebox.showerror('Error', 'No hidden message found. Please hide a message first.')

def show():
    password = code.get()
    if password == user_password:
        try:
            show_msg = lsb.reveal(open_file)
            text1.delete(1.0, END)
            text1.insert(END, show_msg)
        except:
            messagebox.showerror('Error', 'No hidden message found in this image.')
    else:
        messagebox.showerror('Error', 'Incorrect Secret Key')

# Load saved password
load_password()

# UI Components
Label(win, text='steganography', font='impact 30 bold', bg='black', fg='red').place(x=260, y=12)

f1 = Frame(win, width=250, height=220, bd=5, bg='purple')
f1.place(x=50, y=100)
lf1 = Label(f1, bg='purple')
lf1.place(x=0, y=0)

f2 = Frame(win, width=320, height=220, bd=5, bg='white')
f2.place(x=330, y=100)
text1 = Text(f2, font='ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)

Label(win, text='Enter Secret Key', font='10', bg='black', fg='yellow').place(x=250, y=330)
code = StringVar()
e = Entry(win, textvariable=code, bd=2, font='impact 10 bold', show='*')
e.place(x=245, y=360)

# Password Change Section
Label(win, text='Set New Password', font='10', bg='black', fg='lightblue').place(x=450, y=330)
password_entry = Entry(win, bd=2, font='impact 10 bold', show='*')
password_entry.place(x=450, y=360)
Button(win, text='Set Password', bg='lightblue', fg='black', font='ariel 10 bold', cursor='hand2', command=set_password).place(x=470, y=390)

# Buttons
Button(win, text='Open Image', bg='blue', fg='white', font='ariel 12 bold', cursor='hand2', command=open_img).place(x=60, y=417)
Button(win, text='Save Image', bg='green', fg='white', font='ariel 12 bold', cursor='hand2', command=save_img).place(x=190, y=417)
Button(win, text='Hide Data', bg='red', fg='white', font='ariel 12 bold', cursor='hand2', command=hide).place(x=380, y=417)
Button(win, text='Show Data', bg='orange', fg='white', font='ariel 12 bold', cursor='hand2', command=show).place(x=510, y=417)

win.mainloop()


