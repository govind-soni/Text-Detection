# ================================= Importing required libraries =======================================================
from tkinter import *
from tkinter import filedialog
from os import getlogin
from PIL import Image, ImageTk
import cv2
# importing backend code file
# from backend import *

# ============================================== GUI creation ==========================================================
# creating window
app = Tk()

# adding title to it
app.title('Text Recognizer')

# creating a fix sized window
app.geometry('1000x600')
app.resizable(0,0)

# adding background color
app.configure(background='aqua')

# adding brand name using frame
brand_name_frame = Frame(app, bg='aqua', bd=5, relief=RIDGE)
brand_name_frame.pack(side=TOP)

brand_name = Label(brand_name_frame, font=('Consolas Constantia', 30, 'bold'), text='Soniji ka OCR', bg='black',
                   fg='aqua', justify=CENTER)
brand_name.grid(row=0)

# adding welcome label
main_label = Label(app, font=('Arial Black', 42, 'bold'), text='Welcome Buddy 👋', bg='aqua', fg='black')
main_label.place(x=200, y=200)

# adding press any key label
any_key_label = Label(app, font=('Arial Black', 12), text='Press any key to continue.....', bg='aqua', fg='black')
any_key_label.place(x=350, y=550)

# creating variable to store file path
file_path = StringVar()

# # function to get file path
# def filepath():
#     return path
#     #print(path.get())


# creating browse function to upload photo
def browsefiles():
    user_name = getlogin()
    file_name = filedialog.askopenfilename(initialdir='/Users/' + user_name + '/Pictures', title='Select an image',
                                               filetypes=(('JPEG files', ('*.jpeg', '*.jpg')), ('PNG files', '*.png')))
    file_path = file_name

    # getting file name
    filename = file_name.split('/')[len(file_name.split('/')) - 1]

    # creating label to show label name
    file_name_label = Label(app, font=('Arial Black', 9), text=filename, bg='aqua', fg='black')
    file_name_label.place(x=470, y=230, anchor='center')

    # creating ok button
    ok_button = Button(app, text='OK', font=('Arial Black', 8), bg='aqua', fg='black',
                       activebackground='aqua', relief=GROOVE)
    ok_button.place(x=450, y=245)

# function to destroy welcome label and create upload button
def remove_welcome_label(e):
    main_label.destroy()
    any_key_label.destroy()

    # adding instruction about using app
    sub_label = Label(app, font=('Arial Black', 18), text='Upload image by clicking below browse button',
                      bg='aqua', fg='black')
    sub_label.place(x=200, y=90)

    # adding downward arrow label
    arrow_label = Label(app, font=('Arial Black', 24), text='⬇', bg='aqua', fg='black')
    arrow_label.place(x=455, y=120)

    # adding browse button
    browse_button = Button(app, text='Browse', font=('Arial Black', 14), bg='aqua', fg='black', command=browsefiles,
                           activebackground='aqua', relief=GROOVE, width=13)
    browse_button.place(x=380, y=170)

# adding press any key function using bind
app.bind('<KeyPress>', remove_welcome_label)

app.mainloop()