class Inputs:

    def inputInt(self,msg):
        n = -1
        while n < 0:
            try:
                n = int(input(msg))
            except:
                n = -1
                print("Valor invalido!")
        return n