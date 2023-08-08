print(" yours choices are :\n a=add \n b=sub \n c=mul \n d=div \n e=modulus \n f=pow")
option=input("enter your option :")
if option=='a':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("addition is:",a+b)
 if option=='b':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("subtraction is:",a-b)
 if option=='c':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("multiplication is:",a*b)
 if option=='d':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("division is:",a/b)
 if option=='e':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("remender is:",a%b)
 if option=='f':
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    print("power  is:",a**b)
