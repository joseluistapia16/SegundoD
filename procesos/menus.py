from procesos.inputs import *
class MenuD:

    def __init__(self):
        self.ing = Inputs()
    def getMenu(self,opc):
        for i in range(len(opc)):
            print(str(i+1)+".- "+opc[i]+".")
        op = -1
        while op<=0 or op>len(opc):
            op = self.ing.inputInt("Ingrese una opcion[1.."+str(len(opc)) +"]:")
        return op