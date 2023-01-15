#database

from time import time
import videocapture
class StudySession:
    def __init__(self): 
        self.startTime  = time()
        self.time =0
        self.endTime
        #can add modules here
    
    def finished(self):
        self.endTime = time()
        self.time = self.endTime -self.startTime 