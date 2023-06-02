class Metodos:

    def __init__(self,valor):
        self._valor= valor

    def mensaje(self,nombre):
        return "Hola "+nombre

class Arbol:

    def __init__(self, n_hojas,altura,n_ramas):
        self.__n_hojas = n_hojas
        self.altura = altura
        self.n_ramas = n_ramas
        self.public = self.__getPrueba("Andrea")

    def setN_hojas(self,n_hojas):
        self.__n_hojas = n_hojas
    def getN_hojas(self):
        return self.__n_hojas
    def getData(self):
        return str(self.__n_hojas)+" "+str(self.altura)+" "+str(self.n_ramas)

    def __getPrueba(self,nombre):
        return "Hola "+nombre

class Humano:

    def iniciar(self,nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.__curso = curso

    def setCurso(self,curso):
        self.__curso=curso

    def getCurso(self):
        return self.__curso
    def prueba(self,nombre):
        print("Hola "+nombre)

class Persona:

    def __init__(self,cedula,nombre,direccion):
        self.__cedula = cedula
        self.nombre = nombre
        self.direccion = direccion

    def setCedula(self,cedula):
        self.__cedula= cedula

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula + " "+self.nombre+" "+self.direccion

    def getFields(self):
        return None

class Proveedor(Persona):

    def __init__(self,cedula,nombre,direccion,codigo):
        Persona.__init__(self,cedula,nombre,direccion)
        self.codigo = codigo

    def getData(self):
        return "Proveedor:"+self.getCedula()+" "+self.nombre+" "+self.direccion+" "+self.codigo

class Cliente(Persona,Metodos):

    def __init__(self,cedula,nombre, direccion, codigo):
        Persona.__init__(self,cedula,nombre,direccion)
        self.codigo = codigo

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+\
            self.direccion+" "+self.codigo

    def mensaje(self,nombre):
        self._valor = nombre
        print("Hola "+self._valor)

    def getFields(self):
        return  "Cedula:"+self.getCedula()+"\nNombre:"+\
            self.nombre+"\nDireccion:"+self.direccion+"\nCodigo:"+self.codigo

class Producto:

    def __init__(self,codigo,nombre,categoria):
        self.__codigo = codigo
        self.nombre = nombre
        self.categoria = categoria

    def setCodigo(self,codigo):
        self.__codigo= codigo

    def getCodigo(self):
        return self.__codigo

    def getData(self):
        return self.getCodigo()+" "+self.nombre+" "+self.categoria

#Codigo de Prueba




'''
obCl = Cliente("097444","NESTLE","SAMBORONDON","PR001")
obCl.mensaje("Rosario")
print(obCl.getData())

obPr = Proveedor("097444","NESTLE","SAMBORONDON","PR001")
print(obPr.getData())
obPr.direccion="GUASMO"
obPr.setCedula("111111")
print(obPr.getData())

objA = Arbol(20,10.67,40)
print(objA.getData())
objA.altura=34
objA.setN_hojas(100)
print(objA.getN_hojas())
print(objA.public)
print(objA.getData())

obj2 = Humano()
#obj2.nombre= "Carolina"
#obj2.apellido="Chichande"
obj2.iniciar("Carolina","Chichande","2D")
print(obj2.nombre, obj2.apellido,obj2.getCurso())
obj2.setCurso("3D")
print(obj2.nombre, obj2.apellido,obj2.getCurso())
obj2.prueba("Andrea")
'''
