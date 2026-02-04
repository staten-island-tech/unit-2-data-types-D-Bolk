""" x = 3
y = float(3)
print(x,y)
 """



""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0]) """



""" 
number = input("Is this number even or odd")
if int(number) == 1:
    print("Odd")
else:
    print("Even")
 """



def discount(age, isMember, isResident):
    if( age < 12 or age>=65 ) and (isResident or isMember):
        print(discount)