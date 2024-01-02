import cv2 as cv
import numpy as np
import tkinter as tk

cam = cv.VideoCapture(0)

window = tk.Tk()
window.title("Farberkennung")
window.geometry("300x300")

label = tk.Label(window, text="Warte auf Tennisball...")
label.pack()

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # konvertieren in hsv-Farbraum
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Definition Farbbereich
    lower_yellow = np.array([15, 80, 80])
    upper_yellow = np.array([45, 255, 255])

    # Maske für gelbe Objekte
    mask = cv.inRange(hsv, lower_yellow, upper_yellow)

    # Maske auf ursprüngliches Bild
    result = cv.bitwise_and(frame, frame, mask=mask)

    # Kreiserkennung auf result
    grayFrame = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (15, 15), 0)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=5, maxRadius=75)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            cv.circle(frame, (i[0], i[1]), i[2], (200, 0, 255), 3)
        label.config(text="Tennisball gefunden!")
    else:
        label.config(text="Warte auf Tennisball...")

    cv.imshow('Tennisball', frame)
    cv.imshow('Maske', mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


window.mainloop()
cam.release()
cv.destroyAllWindows()



