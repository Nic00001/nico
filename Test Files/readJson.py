import readline
from datetime import datetime

import json


def myappend(file, text):

    with open(file, "a+") as f:
        dt= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {"info" : [
            {'data' : text, 'timestamp' : dt }]}
        
        j= json.dumps(data) 
        
        f.write(j + " \n")

        
def mycreate(file):
    
    with open(file, "w") as f:
        pass 
     
                         
def myread(file):
    
    with open(file, "r") as f:
        
        jason= json.loads(f.read())
        print(jason['info'])
        pass
        



         
            
