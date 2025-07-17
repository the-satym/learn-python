#date: 14 jan 2025


from random import randint
print("guess a number between 1 and 100:")
num=randint(1,100)
while True:
    choose=int(input("enter your guessed no. here:-   "))
    if choose<num:
        print("your guess is lower than actual result.")
    elif choose>num:
        print("your guess is higher than actual result.")
    else:
        print("you have guessed it right!!")
        break
