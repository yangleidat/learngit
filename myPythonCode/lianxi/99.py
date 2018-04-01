first = 1
while first<=9:
    sec = 1    
    while sec <= first:
        print(  str(sec)+"*"+ str(first) +"="+str(sec * first), end="\t")
        sec += 1        
    print()   
    first += 1