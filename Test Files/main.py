#!/usr/bin/end python3

import myLib3 as myLib

def main():
    file= "assignment.txt"
    
    
    while True:
        yesno= input("Read, Write or Append? ")

        if str.lower(yesno) =="quit":
            break 
        
        if yesno == "append":
            text = input("Enter Text1: ")  
            myLib.myappend(file, text)
           
        elif yesno == "read":
            myLib.myread(file)
 
        elif yesno == "write":
            myLib.mycreate(file)            
            
        else:
            continue
           
            

if __name__ == "__main__":
    main()