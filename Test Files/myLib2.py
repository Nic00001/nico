import readline


def myappend(file, text):

    try:
        f = open(file, "a+")
        # f.seek(0,0)
        #raise Exception("Sorry, no numbers below zero")
        f.write(text + "\n")
        f.close()
    except:
        print("X") 
        f.close()
     
        
def mycreate(file):
    try:
        f= open(file, "w")
        # f.write()
        f.close()
    except:
        print("X") 
        f.close()
     
        
                    

def myread(file):
    try:
        f =open(file, "r")
        print (f.readlines())
        f.close()
    except:
        print("X") 
        f.close()
     
            
