import cv2
import time
import database #get classes defined from our database file
import winsound

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

isStudying = False



def backend():
    
    global isStudying #boolean to test if in session
    global currentSession
    currentSession = database.StudySession() #__init__
    
    while True:
        while isStudying:
    
            Studying(currentSession, currentSession.getStartTime())
        
      

def Studying(currentSession, start_time): #once study session is started (start button pressed)
    global isStudying 
    left_time = start_time
    
    session = database.StudySession()
    session = currentSession
    
    AFKcounter = 0 
    x = 20
    timeout = time.time() + x
    
    toggle = False #toggles between gone and not gone. When we go from True(gone) to False(present), AFK counter goes up
    while isStudying:
       

        watervalue = 1800 #1800 Seconds = reminder every 30m to drink water
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
        
            #start_time = time.time()
        
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
        
    #excited while loop -> studying is done  time to record data
    currentSession.finished(AFKcounter) 
    currentSession.output()#testing purposes: outputs data to terminal 


def flip():
    global isStudying
    isStudying = not isStudying


""" if __name__ == "__main__":
    main() """