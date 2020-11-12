def countw(): 
    input1=input("type the file name")
    noofwords = 0
    openfile = open(input1,"r")
    for access in openfile:
        words = access.split()
        noofwords=noofwords+len(words)
    print(noofwords)    
countw()    