class Time():
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.second = self.second + other.second
        return result

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

    def sub(self,other):
        res = Time()
        res.hour = self.hour - other.hour
        res.minute = self.minute - other.minute
        res.second = self.second - other.second

        if res.hour < 0:
            res.hour *= -1
        if res.minute < 0:
            res.minute *= -1
        if res.second < 0:
            res.second *= -1

        return(res)

    def time_to_second(self):
        print((self.hour * 3600) + (self.minute * 60) + self.second)
    
    def second_to_time(self,s):
        self.hour = s // 3600
        s %= 3600
        self.minute = s // 60
        s %= 60
        self.second = s
        self.fix()
        self.show()

# print('*** TIME1 ***')
# time1_h = input("Enter hour : ")
# time1_m = input("Enter minute : ")
# time1_s = input("Enter second : ")

# print('\n*** TIME2 ***')
# time2_h = input("Enter hour : ")
# time2_m = input("Enter minute : ")
# time2_s = input("Enter second : ")

# t1 = Time(time1_h,time1_m,time1_s)
# t2 = Time(time2_h,time2_m,time2_s)

# while True:
#     print('--- MENU ---')
#     print('1- summation')
#     print('2- subtraction')


t1 = Time(17, 51, 40)
t1.show()
t2 = Time(15,32)
t2.show()


a = t1.sum(t2)
a.fix()
print('summation :')
print(a.show())

b = t1.sub(t2)
b.fix()
print('subtraction :')
print(b.show())

#---- converting time to second----
print('first time in second :')
print( t1.time_to_second())

#---- converting secoond to time----
print('second to time :')
print(t1.second_to_time(1700))