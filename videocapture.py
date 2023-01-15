import cv2
import time
from videodetection_modules.leftframe import leftframe
import database #get classes defined from our database file
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)


global isStudying 
global currentSession
isStudying = False

startPressed = True #will be bound to GUI button later, set to True for testing
def main():
    
    currentSession = database.StudySession()
    currentSession.startTime = time.time()
    if startPressed: #start button pressed
        isStudying = True
        
    Studying(currentSession, currentSession.getStartTime())
    
    currentSession.output
    
    
    #exitting loop means stop pressed-> need to reset varriables and track data
    AFKcouner = 0
def Studying(currentSession, start_time): #once study session is started (start button pressed)
    session = database.StudySession()
    session = currentSession
    
    AFKcounter= 0
    while True: #isStudying:
        
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.2, 1)
        
        
        atDesk =leftframe(faces, start_time) #true = at desk, false = not at desk (past 10 seconds buffer)
        if (atDesk):
            print(faces)
        else:
            print("gone")
            AFKcounter+=1


        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        #time.sleep(1)
    # Release the VideoCapture object

        
    cap.release()
    cv2.destroyAllWindows()
        
        
    #excited while loop -> studying is done  time to record data
    currentSession.finished(AFKcounter) 
    #return currentSession
        
    


if __name__ == "__main__":
    main()