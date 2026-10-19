items = {
    "soda": 2.55,
    "pizza": 5.55,
    "pasta": 7,
    "water":10
}
print("-----------MENU-------------")
for key, value in items.items():
    print(f"{key:10} : {value}")

print("----------------------------")
cart = []
result = 0
while True:
    x = input("what YU wanT: ")
    if x == 'q':
        break
    elif x in items:
        cart.append(x)

for i in cart:
    result += items[i]

print(f"total amount is {result}")