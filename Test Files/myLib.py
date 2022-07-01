import readline


def myappend(file, text):
   
    f = open(file, "a")
    
    # f.seek(0,0)
    f.write(text + "\n")
    f.close()
        
def mycreate(file):
    f= open(file, "w")
    # f.write()
    f.close()        

def myread(file):
    f =open(file, "r")
    print (f.readlines())
    f.close()    
