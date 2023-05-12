def getMenu(opc):
    for i in range(len(opc)):
        print(str(i+1)+".- "+opc[i]+".")
    op = 0
    while op<=0 or op>len(opc):
        op = int(input("Ingrese una opcion[1.."+str(len(opc)) +"]:"))
    return op