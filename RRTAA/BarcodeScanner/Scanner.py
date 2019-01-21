from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2


from PIL import Image

# https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/

def decode(im):
    decodedObjects = pyzbar.decode(im)

    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')


    return decodedObjects

def display(im, decodedObjects):
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        n = len(hull)
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

    cv2.imshow("Results", im)
    cv2.waitKey(0)

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        cv2.imwrite("code.png", img)
        im = cv2.imread("code.png", 0)
        decodedObjects = decode(im)
        if len(decodedObjects) != 0 or cv2.waitKey(1) == 27:
            display(im, decodedObjects)
            break  # esc to quit
    cv2.destroyAllWindows()

if __name__ == '__main__':

    user_codes = {}

    show_webcam(mirror=True)

