import readline


def myappend(file, text):

    
    with open(file, "a+") as f:
        # f.seek(0,0)
        #raise Exception("Sorry, no numbers below zero")
        f.write(text + "\n")
        
    #except:
     #   print("X") 
        
     
        
def mycreate(file):
    
    with open(file, "w") as f:
        pass 
     
                         
def myread(file):
    
    with open(file, "r") as f:
        var=  (f.readlines())
        print(var)
        

     
            
