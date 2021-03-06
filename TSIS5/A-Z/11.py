for i in range(65,91):
    with open(chr(i)+'.txt','w') as xt:
        xt.write(chr(i)+' - '+str(i))