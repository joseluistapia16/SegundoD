from dominio.entidades import *
class Procesos:
    def nameRepeat(self,valor,lista):
        res = False
        for i in range(len(lista)):
            if valor== lista[i]:
                res= True
                break
        return res

    def getClient(self,cedula,lista):
        obj = None
        for i in range(len(lista)):
            if cedula== lista[i].getCedula():
                obj = lista[i]
                break
        return obj

    def getClientId(self,cedula, lista):
        pos = -1
        for i in range(len(lista)):
            if cedula== lista[i].getCedula():
                pos = i
                break
        return pos

