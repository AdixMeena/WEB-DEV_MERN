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
while True:
    x = input("what YU wanT: ")
    if x == 'q':
        break
    else:
        cart.append(x)
    