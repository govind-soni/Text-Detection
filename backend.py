# ================================= Importing required libraries =======================================================
import cv2
import pytesseract as pt
import numpy as np
import imutils
import argparse

# configuring pytesseract path
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# ====================================== Function definitions ==========================================================
# function to rotate image
def rotate_image(image):
    for angle in np.arange(0, 360):
        rotated = imutils.rotate_bound(image, angle)
    return rotated

# function for words recognition from image
def words_recognition(image):
    img = cv2.resize(image, (500, 500), None, 0.25, 0.25)
    img = rotate_image(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    boxes = pt.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv2.putText(img, b[-1], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1.2, (40, 40, 255), 2)
    cv2.imshow('WORD RECOGNISED IMAGE', img)
    cv2.waitKey(0)

# function for characters recognition from image
def char_recognition(image):
    img = cv2.resize(image, (500, 500), None, 0.25, 0.25)
    img = rotate_image(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hImg, wImg, _ = img.shape
    boxes = pt.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, hImg - y + 27), cv2.FONT_HERSHEY_COMPLEX, 1.2, (40, 40, 255), 2)
    cv2.imshow('CHARACTER RECOGNISED IMAGE', img)
    cv2.waitKey(0)

# function for digits recognition from image
def number_recognition(image):
    img = cv2.resize(image, (500, 500), None, 0.25, 0.25)
    img = rotate_image(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cong = r'--oem 3 --psm 6 outputbase digits'
    boxes = pt.image_to_data(img, config=cong)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv2.putText(img, b[-1], (x , y), cv2.FONT_HERSHEY_COMPLEX, 1.2, (40, 40, 255), 2)
    cv2.imshow('NUMBER RECOGNISED IMAGE', img)
    cv2.waitKey(0)
