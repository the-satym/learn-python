#date: 14 jan 2025


import time
ts=time.strftime('%H:%M:%S')
a=input("enter your name :-  ")
print(ts)
ts=int(time.strftime('%H'))
if 0<ts<=12:
    print("good morning",a,"its ",ts,"o'clock")
elif 12<ts<=5:
    print("good after noon",a,"its ",ts-12,"o'clock")
elif 5<ts<=8:
    print("good evening",a,"its ",ts-12,"o'clock")
else:
    print("so ja chutiye",a,"its ",ts-12,"o'clock")