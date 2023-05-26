from procesos.menus import *
class Run:

    def __init__(self):
        self.men = MenuD()

    def start(self):
        opc =("REGISTRO", "CONSULTA","ACTUALIZAR",
              "ELIMINAR","LISTADO","SALIR")
        op = self.men.getMenu(opc)

    def __getClient(self,lista, cedula):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].getCedula():
                obj = lista[i]
                break
        return obj
    def prueba(self):
        lista = []
        obCl1 = Cliente("097444", "NESTLE", "SAMBORONDON", "CL001")
        obCl2 = Cliente("012345", "ALMA VELOZ", "DAULE", "CL002")
        obCl3 = Cliente("055678", "CAROLINA CHICHANDE", "ENTRADA DE LA 8", "CL003")
        obCl4 = Cliente("055556", "ROSARIO SERRANO", "CHONGON", "CL004")
        obCl5 = Cliente("091224", "CESAR MERCADO", "PLAYAS", "CL005")
        lista.append(obCl1)
        lista.append(obCl2)
        lista.append(obCl3)
        lista.append(obCl4)
        lista.append(obCl5)
        # print(lista[0].nombre,lista[0].codigo,lista[0].getCedula())
        for i in range(len(lista)):
            print(lista[i].getData())

        ced = input("Cedula:")
        obj = self.__getClient(lista, ced)
        if obj == None:
            print("Cedula no existe!")
        else:
            print(obj.getData())