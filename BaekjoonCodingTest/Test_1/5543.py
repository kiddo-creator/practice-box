menu_ham = []
menu_drink = []

for i in range(3):
    cost1 = int(input())
    menu_ham.append(cost1)

for i in range(2):
    cost2 = int(input())
    menu_drink.append(cost2)

menu_ham.sort()
menu_drink.sort()

print(menu_ham[0]+menu_drink[0]-50)
