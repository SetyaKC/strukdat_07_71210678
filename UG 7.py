class PrefixConverter:
    def __init__(self):
        self._stackList = []

    def push(self,data):
        self._stacklist.append(data)
    
    def peek(self):
        if self.stackList:
            return self._stackList[-1]
        else:
            return "Isi Stack Kosong"
    
    def pop(self):
        if self._stackList:
            data = self._stacklist.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    
    def cekValidExpression(self,expression):
        if expression == "+*-/":
            return True
        else:
            return False

    def infixToPrefix(self,expression):
        prefix = " "
        for i in expression:
            if(len(expression)%2==0):
                print("Expresi Infix yang anda masukan tidak valid!!")
                return False
            elif (self._cekValidExpression(i)):
                prefix +=i
            elif 





if __name__ == '__main__':
expresi1 = PrefixConverter()print(expresi1.infixToPrefix("1+2+3*4/2-1"))
print(expresi1.infixToPrefix("A * (B + C) / D"))
print(expresi1.infixToPrefix("(1+2)*3"))
print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))