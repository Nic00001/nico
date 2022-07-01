

while True:
    yesno= input("Read, Write or Append? ")
    
    if str.lower(yesno) =="quit":
        break


    if yesno == "append":
        text = input("Enter Text: ")
        f = open("desktop\\assignment.txt", "a")
        f.seek(0,0)
        f.write(text + "\n")
        f.close()
    elif yesno == "read":
            import readline
            f =open("desktop\\assignment.txt", "r")
            print (f.readlines())
            f.close()
    else:
            f= open("desktop\\assignment.txt", "w")
            # f.write()
            f.close()
             


