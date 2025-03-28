#exception handling :

try:
    num = int(input("Enter a number : "))
    print(num)
except ValueError as ex:
    print("Exception :",ex)
    
    
print("iam out side try except")

# different exception handling
try:
    n1 = int(input("Enter your number "))
    n2 = int(input("Enter your number "))
    result = n1/n2 
    print("the value of Result is :", result)
except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("please enter numeric value")
except NameError as ex:
    print("please enter numeric value")
except:
    print("Some error occured")
finally:
    print("I will execute no matter exception occurs or no")


valid  = False

while not valid:
    try:
        n = int(input("Enter a number"))
        while n %2 ==0:
            print("Bye num is divided by 2")
            valid = True
    except ValueError:
        print("invalid value")





