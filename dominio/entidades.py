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

#Codigo de Prueba
'''
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
