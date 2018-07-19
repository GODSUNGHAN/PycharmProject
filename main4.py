def tower(n,fro,to,tmp) :
    global counter
    if n > 1:
        tower(n-1,fro,tmp,to)
        counter += 1
        #print("Move from",fro,"to",to)
        tower(n-1,tmp,to,fro)
    else:
        counter += 1
        #print("Move from",fro,"to",to)


counter = 0
tower(20,"A","C","B")
print("The number of move:",counter)
