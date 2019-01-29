import argparse
import imutils
import cv2
from CircleObject import Circle
import numpy as np
import cv2
import time

from cv2.cv2 import putText, FONT_HERSHEY_COMPLEX_SMALL

video = cv2.VideoCapture("../shina.mp4")

cam = video

all_circles = []
id_circle = 0
while True:
    # show_webcam()
    _, frame = cam.read()

    image = frame
    output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 250)
    # circles = cv2.HoughCircles(gray, .cv.CV_HOUGH_GRADIENT, 1.2, 100)

    # ensure at least some circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        time_current = time.time()
        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:

            # if not all_circles:
            #     all_circles.append(Circle(x, y, r, id_circle))
            #     id_circle += 1
            for obj in all_circles:
                cv2.circle(output, (obj.x, obj.y), obj.r, (255, 255, 0), 4)
                cv2.rectangle(output, (obj.x - 5, obj.y - 5),
                              (obj.x + 5, obj.y + 5),
                              (255, 255, 255),
                              -1)

                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 500)
                fontScale = 1
                fontColor = (255, 255, 255)
                lineType = 2

                cv2.putText(output, "{}".format(obj.id), (obj.x, obj.y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                            (255, 255, 255), lineType=cv2.LINE_AA)
            print(len(all_circles))
            # if not all_circles:

            updated = False
            for obj in all_circles:
                print(len(all_circles))

                # print(len(all_circles))
                if time_current - obj.time_created > 0.5:
                    all_circles.remove(obj)
                if obj.update(x, y, r):
                    updated = True
                    break

            if not updated:
                all_circles.append(Circle(x, y, r, id_circle, time.time()))
                id_circle += 1

        # show the output image
        lineThickness = 2
        x1 = 274
        y1 = 7
        x2 = 274
        y2 = 349
        cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), lineThickness)

        cv2.imshow("output", np.hstack([image, output]))

    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
