import cv2
import sys

name = input("Enter the file name(with the file type:")
Ftype = input("What is the file type:")
fileName = name+"."+Ftype

#Add the image and the software
imagePath = fileName
cascPath = "haarcascade_frontalface_default.xml"

#Set up cascade detection
faceCascade = cv2.CascadeClassifier(cascPath)

#Converts the image to grayscale and reads it
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect faces
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (30,30),
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
    
print ("Found {0} faces!".format(len(faces)))

#Draw a rctangle around the images
for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h),(0,255,0),2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
