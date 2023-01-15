#database

from time import time

class StudySession:
    def __init__(self): 
        #only run first time
        self.startTime  = time()
        self.time =0
        self.timesAFK = 0
        #can add modules here
    
    def finished(self, AFKcounter):
        #session is finished, record needed info to the study session
        self.endTime = time()
        self.time = self.endTime -self.startTime 
        self.timesAFK = AFKcounter #record times AFK to the study session
    
    def getStartTime(self):
        #return start time
        return self.startTime
    def output(self):
        #output parameters to terminal, used for testing/debugging pruposes
         print(f'Start Time: {self.startTime}, End Time: {self.endTime}, Session Duration: {self.time}, times AFK {self.timesAFK}')
