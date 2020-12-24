import cv2
cam=cv2.VideoCapture(0)
a,img=cam.read()
cv2.imwrite("/tmp/a.png",img)
cam.release()