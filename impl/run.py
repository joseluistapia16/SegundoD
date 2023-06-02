from procesos.menus import *
from dominio.entidades import *
from  procesos.datos import *
from archivos.archivos import *
class Run:

    def __init__(self):
        self.ruta ="C:/Users/Usuario/PycharmProjects/SegundoD/segundoD.csv"
        self.men = MenuD()
        self.lista = []
        self.pro = Procesos()
        self.arch = Archivo()
        self.lista= self.arch.getClients(self.ruta)


    def start(self):
        opc =("REGISTRO", "CONSULTA","ACTUALIZAR",
              "ELIMINAR","LISTADO","SALIR")
        op = self.men.getMenu(opc)
        if op==1:
            self.__registro()
            self.start()
        if op==2:
            self.__consulta()
            self.start()
        if op== 3:
            self.__actualizar()
            self.start()
        if op==4:
            self.__eliminar()
            self.start()
        if op==5:
            self.__listar()
            self.start()

    def __registro(self):
        print("\tREGISTRO DE CLIENTES")
        self.lista= self.arch.getClients(self.ruta)
        cedula = input("Cedula:")
        pos = self.pro.getClientId(cedula,self.lista)
        if pos==-1:
            nombre = input("Nombre:")
            direccion = input("Direccion:")
            cod = input("Codigo:")
            obj = Cliente(cedula,nombre,direccion,cod)
            msg = obj.getCedula()+";"+obj.nombre+";"\
                  +obj.direccion+";"+obj.codigo+";\n"
            self.arch.create(self.ruta,msg,"a")
            print("Datos guardados!")
        else:
            print("Cedula ya existe!")
        input("<Enter> para continuar...")

    def __listar(self):
        print("\tLISTA DE CLIENTES")
        self.lista= self.arch.getClients(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar...")

    def __consulta(self):
        print("\tCONSULTA DE CLIENTES")
        ced = input("Cedula:")
        self.lista=self.arch.getClients(self.ruta)
        obj = self.pro.getClient(ced,self.lista)
        if obj!=None:
            print(obj.getFields())
        else:
            print("Cedula no existe!!")

        input("<Enter> para continuar...")

    def __actualizar(self):
        print("\tACTUALIZAR DATOS DE CLIENTES")
        ced = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        pos = self.pro.getClientId(ced,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre:")
            direccion = input("Direccion:")
            cod = input("Codigo:")
            self.lista[pos].nombre = nombre
            self.lista[pos].direccion= direccion
            self.lista[pos].codigo = cod
            msg =""
            for i in range(len(self.lista)):
                msg = msg+self.lista[i].getCedula()+";"+self.lista[i].nombre+";"\
                      +self.lista[i].direccion+";"+self.lista[i].codigo+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos actualizados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")

    def __eliminar(self):
        print("\tELIMINAR DATOS DE CLIENTES")
        ced = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        pos = self.pro.getClientId(ced,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            self.lista.pop(pos)
            msg =""
            for i in range(len(self.lista)):
                msg= msg+self.lista[i].getCedula()+";"+self.lista[i].nombre+";"\
                     +self.lista[i].direccion+";"+self.lista[i].codigo+";\n"
            #print(msg)
            self.arch.create(self.ruta,msg,"w")
            print("Datos eliminados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")



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