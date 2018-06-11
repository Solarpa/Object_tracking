import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import imutils
import time
from imutils.video import WebcamVideoStream

 # Find barcodes and QR codes
def decode(im) :

  decodedObjects = pyzbar.decode(im)
  return decodedObjects

  # Loop over all decoded objects
def display(im, decodedObjects):

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



print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0)
time.sleep(2.0)


while True:
    # Capture frame-by-frame
    ret, image = cap.read()
    image= imutils.resize(image, width=400)
    decodedObjects=decode(image)
    display(image, decodedObjects)
    cv2.imshow("Results", image);


    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break



cv2.destroyAllWindows()
