file = open("./myinfo.txt","a")
send = input('Enter a line of Text: ')
file.write("\n"+send)
file.close()