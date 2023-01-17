import cv2
import time
import StudySession 
import winsound

# Load the cascade
face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')

# Capture video from webcam. 
cap = cv2.VideoCapture(0)

def backend():
    #global isStudying boolean to test if in session
    global currentSession
    currentSession = StudySession.StudySession() #__init__
    Studying(currentSession.getStartTime())
    currentSession.finished(AFKcounter) 
    currentSession.output()
        
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
      

def Studying(start_time): #once study session is started (start button pressed)
    global isStudying , AFKcounter
    left_time = start_time
    
    AFKcounter = 0 
    x = 30
    timeout = time.time() + x
    
    toggle = False #toggles between gone and not gone. When we go from True(gone) to False(present), AFK counter goes up
    while True:
        if time.time()>timeout:
           break #stop studying loop
             
        watervalue = 15 #frequency timer to remind user to drink water
        if (int((time.time())+1) % watervalue == 0):
            winsound.PlaySound("assets/recording", winsound.SND_FILENAME) #playing sound
            
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect face
        faces = face_cascade.detectMultiScale(gray, 1.2, 1)
        
        #atDesk: true = at desk, false = not at desk (past 2 second buffer)
        if (type(faces) == tuple): 
            if (time.time()-left_time > 2):
                atDesk = False #left 
            else:
                atDesk =  True
        else :
            left_time = time.time()
            atDesk = True
        
        if (atDesk):
            toggle = False #present at desk
        else:
            if (toggle == False):
                AFKcounter += 1 #we have changed from present to gone
                print("Hey! Get back to work!")
            toggle = True #gone