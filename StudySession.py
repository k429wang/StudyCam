from time import time

class StudySession:
    def __init__(self): 
        #only run first time
        self.startTime = time()
        self.time = 0
        self.timesAFK = 0
        #can add more modules here
    
    def finished(self, AFKcounter):
        #session is finished, record needed info to the study session
        self.endTime = time()
        self.time = self.endTime - self.startTime 
        self.timesAFK = AFKcounter #record times AFK to the study session
    
    def getStartTime(self):
        #return start time
        return self.startTime
        
    def output(self):
        #output parameters to terminal, used for testing/debugging pruposes
        print(f'You are done Studying, you have been studying for {self.time} seconds. You have taken {self.timesAFK} breaks during your study session! ')