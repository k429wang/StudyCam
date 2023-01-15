from time import time #time module (makes it easier to define things and we are using time anyway so better to record in seconds)

def leftframe(faces,left_time):
    if (type(faces) == tuple): 
        
        if (time() - left_time > 10):
              return False #left 
        #return True
    else :
        left_time = time()
    return True
      
        
       
   