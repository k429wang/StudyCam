import cv2
import time
from videodetection_modules.leftframe import leftframe

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)


def main():
    start_time = time.time()
    while True:
        counter = 0
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.2, 1)
        
        
        x = leftframe(faces, time)
        if not x:
            start_time = time.time()
        if (time.time() - start_time >= 5 ):
            print("WHY ARENT UUUU HERE!!!1")
        else:
            print(faces)


        #  for (x, y, w, h) in faces:
        #      cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #  cv2.imshow('img',img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        #time.sleep(1)
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()