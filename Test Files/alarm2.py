import datetime

current_time = datetime.datetime.now()
now = current_time.strftime("%H_%M")
a= now

file= a+'.txt'
def createNew(file):
    with open(file, 'w')as f:
        pass


def writein(file):
    with open(file, 'a')as f:
        f.write("hek\n")
   
        pass

    
 