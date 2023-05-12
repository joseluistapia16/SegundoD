def suma(x1,x2):
    r = (x1+x2)
    return r

def getMessage(pr):
    if pr>10 or pr<0:
        return "Valor invalido!"
    else:
        if pr>=0 and pr<7:
            return "Reprobado"
        if pr>=7 and pr<=10:
            return "Aprobado"
def getPromedio(n1,n2,n3):
    return (n1+n2+n3)/3
def getAge(edad):
    if edad<0 or edad>110:
        return "Edad incorrecta"
    else:
        if edad>0 and edad<11:
            return "infante"
        if edad>10 and edad<18:
            return "Adolescente"
        if edad>17 and edad<26:
            return  "Joven"
        if edad>25 and edad<65:
            return  "Adulto"
        if edad>64:
            return "Adulto mayor"
