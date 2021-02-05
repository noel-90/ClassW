# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

#float data Type
#Floats = real numebers with decimal poinst

num =3.14
print(type(num))
#example of float
AmountOfPeople =12
AmountofMoney =13423
AmountForEachPerson = AmountofMoney / AmountOfPeople
print(AmountForEachPerson)

formatedAmountforEachPerson= format(AmountForEachPerson,".3f")
print(formatedAmountforEachPerson)

print(10.3)
print(type(10.3))
print(5e-4)

# integer numbers with right alignment
print("{:5d}".format(12))

# float numbers with center alignment
print("{:^10.3f}".format(12.2346))

# integer left alignment filled with zeros
print("{:<05d}".format(12))
# float numbers with center alignment
print("{:=8.3f}".format(-12.2346))

##Deep Dive: inf and NaN

x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))
y = float('Inf')
print('%f, %e, %F, %E' % (y, y, y, y))

x=8.7
y=3.5
z=x+y
print(z)







