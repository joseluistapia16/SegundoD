def nameRepeat(valor,lista):
    res = False
    for i in range(len(lista)):
        if valor== lista[i]:
            res= True
            break
    return res