# ================================= Importing required libraries =======================================================
from tkinter import *
from tkinter import filedialog
from os import getlogin
from PIL import Image, ImageTk
import cv2
# importing backend code file
from backend import *

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

# creating variable to store values
file_path = None
browse_button = None
file_name_label = None
ok_button = None
sub_label = None
arrow_label = None
cancel_button = None
choice_label = None
word_recognition_button = None
char_recognition_button = None
num_recognition_button = None
reupload_button = None

# creating function to store
def remove_upload_label():
    global choice_label, word_recognition_button, char_recognition_button, num_recognition_button, reupload_button
    sub_label.destroy()
    arrow_label.destroy()
    browse_button.destroy()
    file_name_label.destroy()
    ok_button.destroy()
    cancel_button.destroy()

    #creating user choice label
    choice_label = Label(app, font=('Arial Black', 24), text='Choose a operation', bg='aqua', fg='black')
    choice_label.place(x=340, y=130)

    # reading image
    image = cv2.imread(file_path)

    # creating button for words recognition
    word_recognition_button = Button(app, text='Click to recognize words', font=('Arial Black', 16), bg='aqua',
                                     fg='black', command=lambda :words_recognition(image), activebackground='aqua',
                                     relief=GROOVE, width=35)
    word_recognition_button.place(x=220, y=200)

    # creating button for characters recognition
    char_recognition_button = Button(app, text='Click to recognize characters', font=('Arial Black', 16), bg='aqua',
                                     fg='black', command=lambda: char_recognition(image), activebackground='aqua',
                                     relief=GROOVE, width=35)
    char_recognition_button.place(x=220, y=260)

    # creating button for numbers recognition
    num_recognition_button = Button(app, text='Click to recognize numbers', font=('Arial Black', 16), bg='aqua',
                                     fg='black', command=lambda: number_recognition(image), activebackground='aqua',
                                     relief=GROOVE, width=35)
    num_recognition_button.place(x=220, y=320)

    # creating re upload button
    reupload_button = Button(app, text='Click to Re-upload new image', font=('Arial Black', 16), bg='aqua', fg='black',
                             command=lambda :remove_operation_label('<Button-1>'), activebackground='aqua',
                             relief=GROOVE, width=35)
    reupload_button.place(x=220, y=390)


def remove_operation_label(e):
    global browse_button, sub_label, arrow_label
    choice_label.destroy()
    word_recognition_button.destroy()
    char_recognition_button.destroy()
    num_recognition_button.destroy()
    reupload_button.destroy()

    # adding instruction about using app
    sub_label = Label(app, font=('Arial Black', 18), text='Upload image by clicking below browse button',
                      bg='aqua', fg='black')
    sub_label.place(x=200, y=210)

    # adding downward arrow label
    arrow_label = Label(app, font=('Arial Black', 24), text='⬇', bg='aqua', fg='black')
    arrow_label.place(x=455, y=240)

    # adding browse button
    browse_button = Button(app, text='Browse', font=('Arial Black', 14), bg='aqua', fg='black', command=browsefiles,
                           activebackground='aqua', relief=GROOVE, width=16)
    browse_button.place(x=360, y=290)


# creating function to reupload file
def cancel_upload():
    global file_name_label, file_path, ok_button, cancel_button, browse_button
    file_name_label.destroy()
    ok_button.destroy()
    cancel_button.destroy()
    file_path = None
    browse_button['state'] = 'normal'

# creating browse function to upload photo
def browsefiles():
    global file_name_label, ok_button, file_path, cancel_button, browse_button
    user_name = getlogin()
    file_name = filedialog.askopenfilename(initialdir='/Users/' + user_name + '/Pictures', title='Select an image',
                                               filetypes=(('JPEG files', ('*.jpeg', '*.jpg')), ('PNG files', '*.png')))
    file_path = file_name
    # getting file name
    filename = file_name.split('/')[len(file_name.split('/')) - 1]

    # disabling browse button for further operation
    browse_button['state'] = 'disabled'
    browse_button['disabledforeground'] = 'black'

    # creating label to show label name
    file_name_label = Label(app, font=('Arial Black', 9), text=filename, bg='aqua', fg='black')
    file_name_label.place(x=470, y=350, anchor='center')

    # creating ok button
    ok_button = Button(app, text='OK', font=('Arial Black', 9), bg='aqua', fg='black', command=remove_upload_label,
                               activebackground='aqua', relief=GROOVE, width=12)
    ok_button.place(x=360, y=365)

    # creating cancel button to reupload file
    cancel_button = Button(app, text='CANCEL', font=('Arial Black', 9), bg='aqua', fg='black', command=cancel_upload,
                                   activebackground='aqua', relief=GROOVE, width=12)
    cancel_button.place(x=473, y=365)

# function to destroy welcome label and create upload button
def remove_welcome_label(e):
    global browse_button, sub_label, arrow_label
    main_label.destroy()
    any_key_label.destroy()

    # adding instruction about using app
    sub_label = Label(app, font=('Arial Black', 18), text='Upload image by clicking below browse button',
                      bg='aqua', fg='black')
    sub_label.place(x=200, y=210)

    # adding downward arrow label
    arrow_label = Label(app, font=('Arial Black', 24), text='⬇', bg='aqua', fg='black')
    arrow_label.place(x=455, y=240)

    # adding browse button
    browse_button = Button(app, text='Browse', font=('Arial Black', 14), bg='aqua', fg='black', command=browsefiles,
                           activebackground='aqua', relief=GROOVE, width=16)
    browse_button.place(x=360, y=290)

# adding press any key function using bind
app.bind('<KeyPress>', remove_welcome_label)

app.mainloop()
