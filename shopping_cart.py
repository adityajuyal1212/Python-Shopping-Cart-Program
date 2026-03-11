# Shopping Cart Program

food = {"burger" : 7,
        "hamburger" : 10,
        "pizza" : 16, 
        "coke" : 5}

cart = []
total = 0

print("--------MENU--------")
for key, value in food.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    order = input("Enter your order (q to quit):")
    if order.lower()=="q":
        break

    elif food.get(order) is not None:
        cart.append(order)

print("------YOUR ORDER------")
for order in cart:
    total += food.get(order)
    print(order, end=" ")

print() 
print(f"Your total is ${total:.2f}")

print("--------------------")
