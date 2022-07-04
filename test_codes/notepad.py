
username = input("Enter Text: ")
f = open("desktop\\assignment.txt", "a")
f.write("\n" + username)
f.close()

