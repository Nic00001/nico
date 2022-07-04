#!/usr/bin/end python3

import readJson as myLib

def main():
    file= "Json_text.json"
     
    while True:
        yesno= input("Read, Write or Append?:    ")

        if str.lower(yesno) =="done":
            break 
        
        if yesno == "append":
           # while True:
                text = input("Enter Text: ")  
                myLib.myappend(file, text)
            #    if (text)== "done":
            #       break
           
        elif yesno == "read":
            myLib.myread(file)
 
        elif yesno == "write":
            myLib.mycreate(file)         
              
            
        else:
            continue
           
            

if __name__ == "__main__":
    main()