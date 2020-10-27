def scaner(comando):
    dicio={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    if len(comando)==4:
        rowe=int(comando[1])-1
        collune=dicio[comando[0].upper()]
        rowv=int(comando[3])-1
        collunv=dicio[comando[2].upper()]
        return rowe,collune,rowv,collunv
    if len(comando)==2:
        rowe=int(comando[1])-1
        collune=dicio[comando[0].upper()]
        return rowe,collune


    

