#from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import imutils
import time
import threading

###
def decode(im) :
  # Find barcodes and QR codes
  decodedObjects = pyzbar.decode(im)

  ## Print results
  # for obj in decodedObjects:
  #   print('Type : ', obj.type)
  #   print('Data : ', obj.data,'\n')

  return decodedObjects
# Display barcode and QR code location
def display(im, decodedObjects):

  # Loop over all decoded objects
  for decodedObject in decodedObjects:
    points = decodedObject.polygon

    # If the points do not form a quad, find convex hull
    if len(points) > 4 :
      hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
      hull = list(map(tuple, np.squeeze(hull)))
    else :
      hull = points;
    # Number of points in the convex hull
    n = len(hull)

    # Draw the convext hull
    for j in range(0,n):
      cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)



def find_frame():
    global image
    global stopper
    print("[INFO] starting video stream...")
    cap = cv2.VideoCapture(0)
    time.sleep(2.0)
    while stopper:
        ret, image = cap.read()




global image
global stopper
stopper =True

video_thread=threading.Thread(target=find_frame)
video_thread.start()

time.sleep(3.0)
while True:
    # grab the frame from the threaded video stream
    # Capture frame-by-frame
    decodedObjects=decode(image)
    display(image, decodedObjects)
    cv2.imshow("Results", image);

    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        stopper =False
        break
    ####


cv2.destroyAllWindows()
