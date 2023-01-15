import cv2
import time
#from videodetection_modules.leftframe import leftframe
import database #get classes defined from our database file
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)



isStudying = False

startPressed = True #will be bound to GUI button later, set to True for testing
def main():
    global isStudying #boolean to test if in session
    global currentSession
    currentSession = database.StudySession() #__init__
    
    if startPressed: #start button pressed
        isStudying = True
    
    
    
        
    Studying(currentSession, currentSession.getStartTime())
    
    
    
    
    #exitting loop means stop pressed-> need to reset varriables and track data
    AFKcouner = 0
def Studying(currentSession, start_time): #once study session is started (start button pressed)
    global isStudying 
    left_time = start_time

    
    session = database.StudySession()
    session = currentSession
    
    AFKcounter= 0 
    x = 20
    timeout = time.time()+x
    
   
    toggle = False #toggles between gone and not gone. When we go from True(gone) to False(present), AFK counter goes up
    while isStudying:
       
        if time.time()>timeout:
        #timer for testing - simulates someone pressing stop after x seconds (will be swapped to button later so dw about this)
            isStudying=False#stop studying loop
            
        
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.2, 1)
       
        #atDesk: true = at desk, false = not at desk (past 10 seconds buffer)
        if (type(faces) == tuple): 
            if (time.time() - left_time >3):
                atDesk= False #left 
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
                AFKcounter+=1 #we have changed from present to gone
            toggle = True #gone
            print("gone")
        
            #start_time = time.time()


        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
        
    # Release the VideoCapture object

    cap.release()
    cv2.destroyAllWindows()
        
        
    #excited while loop -> studying is done  time to record data
    currentSession.finished(AFKcounter) 
    currentSession.output()#testing purposes: outputs data to terminal 
        
    


if __name__ == "__main__":
    main()