class fraction(object):
    def __init__(self, s = 0, m = 1):
        self.s = s
        if m!= 0:
            self.m = m
        else:
            self.m = 1

    def show(self):
        print(self.s,'/',self.m)

    def mul(self,y):
        result  = fraction()
        result.s = self.s * y.s
        result.m = self.m * y.m
        return result
        
    def sum(self,other):
        result = fraction()
        result.s = self.s * other.m + self.m * other.s
        result.m = self.m * other.m
        return result

    def sub(self,other):
        result = fraction()
        result.s = self.s * other.m - self.m * other.s
        result.m = self.m * other.m
        return result

    def div(self,other):
        result = fraction()
        result.s = self.s * other.m
        result.m = self.m * other.s
        return result

    def simp(self):
        for i in range(1,10):
            if self.s % i == 0 and self.m % i == 0:
                self.s = self.s / i 
                self.m = self.m / i 
        res = self.s,'/',self.m
        return res
            
a = fraction(2,8)
a.show()

b = fraction(3,4)
b.show()

#-----Multiplication-----
c = a.mul(b)
c.show()

#-----Summation-----
d = a.sum(b)
d.show()

#-----Subtraction-----
e = a.sub(b)
e.show()

#-----Division-----
f = a.div(b)
f.show()

#-----Simplification-----
g = a.simp()
print(g)