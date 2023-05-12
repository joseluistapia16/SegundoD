from procesos.operaciones import *
from procesos.datos import *
from procesos.menus import *
def funcion2():
    v1 = "Hola"+" "+"Segundo D"
    v2 = " POO "
    v3 = v1+v2
    print(v3)
def funcion3():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    r = suma(n1,n2)
    print("Total :"+str(r))
def funcion4():
    edad = int(input("Edad:"))
    res = getAge(edad)
    print(res)

def funcion5():
    c=0
    ci=0
    ac = 0
    while c<19:
        c = c+1
        if c%2!=0:
         print(c)
         ci = ci +1
         ac = ac +c

    print("Cantidad de impares es:"+str(ci))
    print("Total acumulado:"+str(ac))

    c=0
    ac=0
    for i in range(1,20):
        if i%2!=0:
          print(i)
          c= c +1
          ac = ac + i
    print("Cantidad de impares es:"+str(c))
    print("Total acumulado:"+str(ac))
def funcion6():
    datos = (False,"Jose",200,True,100)
    for i in range(len(datos)):
        print(datos[i])

    data = [5,7,3]
    data.append("POO")
    data.append(False)
    data.append("BASE DE DATOS")
    data[1]=700
    #data.pop(2)
    del data[4]
    #print(data)
    for i in range(len(data)):
        print(data[i])
    print("Tamaño :"+str(len(data)))
    data.clear()
    print("Tamaño :"+str(len(data)))

    dic = {
        "josed" : 60,
        100 : "POO",
        True : [3,4,5],
        (4,7,8):"2D"
    }
    dic[100] = "INGLES"
    dic["Andrea"]= True
    del dic[True]
    print(dic)

def funcion7():
    nombre = input("Nombre:")
    materia = input("Materia:")
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    n3 = float(input("Nota 3:"))
    pr = getPromedio(n1,n2,n3)
    msg = getMessage(pr)
    print("El promedio es:"+str(pr))
    print(msg)


def funcion1():
    print("Hola ")
    print("2D")
    funcion2()

def funcion8():
    lista =[]
    c=0
    while c< 5:
        nombre = input("Nombre "+str(c+1)+":")
        res = nameRepeat(nombre,lista)
        if res != True:
          lista.append(nombre)
        else:
          c= c-1
          print("Nombre Ya existe!")
        c = c+1
    for i in range(len(lista)):
        print(lista[i])

def funcion9():
    opc =("Registro","Consulta","Actualizar",
          "Eliminar","Lista","Salir")
    op=getMenu(opc)
    if op== 1:
        print("Python")
        input("<Pulse una tecla para continuar..>")
        funcion9()
    if op==2:
        print("Java")
        input("<Pulse una tecla para continuar..>")
        funcion9()

funcion9()


