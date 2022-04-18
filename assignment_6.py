
print("Please select the desired operation:")
print("1-sum\n2-Submission\n3-Multiplication\n4-Division\n5-Simplification")
select = int(input())


class Calculations:
    def __init__(self):
        self.numerator1 = int(
            input("Enter the numerator of the first fraction:\n"))
        self.denominator1 = int(
            input("Enter the denominator of the first fraction:\n"))
        self.numerator2 = int(
            input("Enter the numerator of the second fraction:\n"))
        self.denominator2 = int(
            input("Enter the denominator of the second fraction:\n"))

    def su_m(self):
        if self.denominator1 == self.denominator2:
            out_put1 = self.numerator1+self.numerator2
            print(out_put1, "/", self.denominator1)
        else:
            out_put2 = self.denominator1*self.denominator2
            num1 = self.denominator2*self.numerator1
            num2 = self.denominator1*self.numerator2
            out_put3 = num1+num2
            print(out_put3, "/", out_put2)

    def sub(self):
        if self.denominator1 == self.denominator2:
            out_put1 = self.numerator1-self.numerator2
            print(out_put1, "/", self.denominator1)
        else:
            out_put2 = self.denominator1*self.denominator2
            num1 = self.denominator2*self.numerator1
            num2 = self.denominator1*self.numerator2
            out_put3 = num1-num2
            print(out_put3, "/", out_put2)

    def multi(self):
        out_put1 = self.numerator1*self.numerator2
        out_put2 = self.denominator1*self.denominator2
        print(out_put1, "/", out_put2)

    def divi(self):
        out_put1 = self.numerator1*self.denominator2
        out_put2 = self.numerator2*self.denominator1
        print(out_put1, "/", out_put2)


def Formula(x, y):
    if (x < y):
        temp = x
        x = y
        y = temp
    while (y != 0):
        remainder = x % y
        x = y
        y = remainder

    r = x
    return r


class Simplification():
    def __init__(self):
        self.numerator = int(input("Enter the numerator of the fraction\n"))
        self.denominator = int(
            input("Enter the denominator of the fraction\n"))

    def simpl(self):
        n2 = int(self.numerator / Formula(self.numerator, self.denominator))
        d2 = int(self.denominator / Formula(self.numerator, self.denominator))
        print(n2, '/', d2)


if select == 1:
    summ = Calculations()
    summ.su_m()
if select == 2:
    subb = Calculations()
    subb.sub()
if select == 3:
    multii = Calculations()
    multii.multi()
if select == 4:
    divii = Calculations()
    divii.divi()
if select == 5:
    simpll = Simplification()
    simpll.simpl()
