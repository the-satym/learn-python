#date:  13 jan 2025

rerun=input("if you want to use calculator again, enter 'y' for yes and 'n':-   ")
while rerun=="y":
    print("enter 1 for addition ")
    print("enter 2 for substraction")
    print("enter 3 for multiplication")
    print("enter 4 for division ")
    op=int(input("enter the operation no. you want to perform:- "))
    if op==1:
        a=int(input("enter your first no. :- "))
        b=int(input("enter your second no. :- "))
        print("the addition of given two no. are ",a+b)
    elif op==2:
        a=int(input("enter your first no. :- "))
        b=int(input("enter your second no. :- "))
        print("the substraction of given two no. are ",a-b)
    elif op==3:
        a=int(input("enter your first no. :- "))
        b=int(input("enter your second no. :- "))
        print("the multiplication of given two no. are ",a*b)
    elif op==4:
        a=int(input("enter your first no. :- "))
        b=int(input("enter your second no. :- "))
        print("the division of given two no. are ",a/b)
    else:
        print("error! choosed operation does not exist")
