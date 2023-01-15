import cv2
import time
import database #get classes defined from our database file
import winsound

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

def backend():
    isStudying = True
    #global isStudying #boolean to test if in session
    global currentSession
    currentSession = database.StudySession() #__init__
    Studying(currentSession, currentSession.getStartTime())
    currentSession.finished(AFKcounter) 
    currentSession.output()#testing purposes: outputs data to terminal 
        
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
      

def Studying(currentSession, start_time): #once study session is started (start button pressed)
    global isStudying , AFKcounter
    left_time = start_time
    
    session = database.StudySession()
    session = currentSession
    
    AFKcounter = 0 
    x = 20
    timeout = time.time() + x
    
    toggle = False #toggles between gone and not gone. When we go from True(gone) to False(present), AFK counter goes up
    while True:
        if time.time()>timeout:
        #timer for testing - simulates someone pressing stop after x seconds (will be swapped to button later so dw about this)
           break#stop studying loop
             
        watervalue = 10 #1800 Seconds = reminder every 30m to drink water
        if (int((time.time())+1) % watervalue == 0):
            winsound.PlaySound("New Recording 2", winsound.SND_FILENAME) #playing sound
            
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect face
        faces = face_cascade.detectMultiScale(gray, 1.2, 1)
        
        #atDesk: true = at desk, false = not at desk (past 10 seconds buffer)
        if (type(faces) == tuple): 
            if (time.time()-left_time > 3):
                atDesk = False #left 
            else:
                atDesk =  True
        
        else :
            left_time = time.time()
            atDesk = True
        
        if (atDesk):
            toggle = False #present at desk
            print(faces)
        else:
            if (toggle == False):
                AFKcounter += 1 #we have changed from present to gone
            toggle = True #gone
            print("gone")

def flip():
    global isStudying
    isStudying = True

def _ss_value(): #pass isStudying val
    return isStudying