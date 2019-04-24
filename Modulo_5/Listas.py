pizza = ['jamon', 'queso', 'champiñon']
print(pizza)

print(pizza[0])

print(pizza[-1])

print(pizza[1:])

pizza.append('pollo')

print(pizza)

pizza.insert(2, 'queso')

print(pizza)

pizza.pop()

print(pizza)

pizza.remove('queso')

print(pizza)

# pizza.sort()
#
# print(pizza)

pizza_2 = sorted(pizza)

print(pizza_2)

pizza_2 = pizza.copy()

print(pizza_2)

pizza_3 = pizza + pizza_2

print(pizza_3)

print(pizza * 4)

print('queso' in pizza)

print(len(pizza_3))

pizza.reverse()

print(pizza)