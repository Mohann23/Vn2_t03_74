'''
#python program to check leap year using class function

class CodesCracker:
    def checkLeapOrNot(self, x):
        if y % 4 == 0 and y % 100 != 0:
            return 1
        elif y % 400 == 0:
            return 1

print("Enter the Year: ", end="")
y = int(input())

ob = CodesCracker()
chk = ob.checkLeapOrNot(y)
if chk==1:
    print("Leap Year")
else:
    print("Not a Leap Year")
'''

'''
# Define a class for Checking Armstrong number
class Check:

    def __init__(self, number):
        self.num = number

    def isArmstrong(self):
        temp = self.num
        res = 0
        while (temp != 0):
            rem = temp % 10
            res += rem ** 3
            temp //= 10

        if self.num == res:
            print(self.num, "is Armstrong")
        else:
            print(self.num, "is not Armstrong")

if __name__ == "__main__":
    # input number
    num = 153
    check_Armstrong = Check(num)
    check_Armstrong.isArmstrong()

    num = 127
    check_Armstrong = Check(num)
    check_Armstrong.isArmstrong()
'''

'''
#Python Program to Make a Simple Calculator

class Cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b

a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))
obj=Cal(a,b)
while True:
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide')
        print(x)
    menu()
    choice = int(input('Please select one of the following : '))
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 3:
        print("Result: ",obj.multiply())
    elif choice == 4:
        print("Result: ",obj.divide())
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option')
        break
print()
'''

'''
#roman number To Integer

class Py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

print(Py_solution().roman_to_int('IV'))
print(Py_solution().roman_to_int('ML'))
print(Py_solution().roman_to_int('X'))
'''



















