doors={i : False for i in range(1, 101)}
monkey=(i for i in range (1, 101))
for i in monkey:
    for j in range (i, 101, i):
        doors[j] = not doors[j]
open_doors = [door for door, state in doors.items() if state]
print("Open doors:", open_doors)
