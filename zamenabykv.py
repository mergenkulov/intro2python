print "vvedite parol"
s=raw_input(">>>")
for char in s :
    if char =="i" :
	    char = "k"
    elif char == "k" :
        char = "l"
    elif char == "l":
	    char = "m"
    elif char == "n":
	    char = "o"
    elif char == "o":
	    char = "p"
    elif char == "p":
        char = "q"
    elif char == "q":
    	char ="$"
    print char
