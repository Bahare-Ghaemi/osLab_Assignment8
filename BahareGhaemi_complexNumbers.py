class complexNumber:
    def __init__(self, i = 0, r = 0):
        self.img = i
        self.re = r

    def add(self, other):
        res = complexNumber()
        res.img = self.img + other.img
        res.re = self.re + other.re
        return res
    
    def sub(self, other):
        res = complexNumber()
        res.img = self.img - other.img
        res.re = self.re - other.re
        return res

    def mul(self,other):
        res = complexNumber()
        res.img = (self.img * other.img) - (self.re * other.re)
        res.re = (self.re * other.img) - (self.img * other.re)
        return res
        
    def show(self):
        if self.re >= 0:
            print(self.img, "+" , self.re,'i')
        else:
            print(self.img, self.re, 'i')
        

num1 = complexNumber(2,6)
num2 = complexNumber(3,4)

num3 = num1.add(num2)
print('Summation :')
num3.show()

num4 = num1.sub(num2)
print('Subtraction :')
num4.show()

num5 = num1.mul(num2)
print('Multiplication :')
num5.show()