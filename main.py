'''
v1 = "Hola"+" "+"Segundo D"
v2 = " POO "
v3 = v1+v2
print(v3)

n1 = int(input("Numero 1:"))
n2 = int(input("Numero 2:"))
r = (n1+n2)
print("Total :"+str(r))
'''
edad = int(input("Edad:"))
if edad<0 or edad>110:
    print("Edad incorrecta")
else:
    if edad>0 and edad<11:
        print("infante")
    if edad>10 and edad<18:
        print("Adolescente")
    if edad>17 and edad<26:
        print("Joven")
    if edad>25 and edad<65:
        print("Adulto")
    if edad>64:
        print("Adulto mayor")

