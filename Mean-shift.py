import numpy as np
import cv2
video = cv2.VideoCapture("VideoTry_3.mov")



cam = cv2.VideoCapture(0)
_,first_frame = cam.read()
x = 0
y = 17
width = 150	
height = 150

# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror: 
#             img = cv2.flip(img, 1)
#         cv2.imshow('my webcam', img)
#         if cv2.waitKey(1) == 27: 
#             break  # esc to quit
#     cv2.destroyAllWindows()



roi = first_frame[y: y + height, x: x + width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
 
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
 
while True:
    # show_webcam()
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
 
    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("roi", roi)
    cv2.imshow("first_frame", first_frame)

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
video.release()
cv2.destroyAllWindows()