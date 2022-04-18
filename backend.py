# ================================= Importing required libraries =======================================================
import cv2
import pytesseract as pt

# configuring pytesseract path
pt.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# ====================================== Function definitions ==========================================================
# function for words recognition from image
def words_recognition(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    wImg, hImg, _ = img.shape
    boxes = pt.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv2.putText(img, b[-1], (x, y ), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow('IMAGE', img)
    cv2.waitKey(0)

# function for characters recognition from image
def char_recognition(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    wImg, hImg, _ = img.shape
    boxes = pt.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, wImg - y), (w, wImg - h), (0, 0, 255), 2)
        cv2.putText(img, b[0], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow('IMAGE', img)
    cv2.waitKey(0)

# function for digits recognition from image
def number_recognition(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    wImg, hImg, _ = img.shape
    cong = r'--oem 3 --psm 6 outputbase digits'
    boxes = pt.image_to_data(img, config=cong)
    # print(boxes)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 2)
                cv2.putText(img, b[-1], (x , y ), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
    cv2.imshow('IMAGE', img)
    cv2.waitKey(0)
