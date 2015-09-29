print "Pered toboy dve dveri. #1 oDna TemnAYa, #2 vtoraya SvetlaYA"
door=raw_input(">>>")

if door == "1":
    print "Tam SIdit zek, i kuwaet buter. TvoI deistviya"
    print "1. Zaberesh buter"
    print "2. Udarish zeka"

    zek=raw_input(">>>")
    if zek == "1":
        print "On tebya s'el"
    elif zek == "2":
        print "On ZAstavil tebya Zarezatsya"
    else:
        print "on tebya priznal"

elif door == "2":
    print "Stoit sTol , Na sTole zvonit telefon. Vashi deistviya"
    print "1. Podnimesh trubku"
    print "2. otmenish vyzov"
    print "Razbil telefoN"

    trubka=raw_input(">>>")

    if trubka== "1" or trubka== "2":
        print "teBe Zvonit zeK iz sosedney komnaty"
    else:
    	print "Zek PRisheL k TEbe"
else:
    print "YOU WIN. GAME OVER"