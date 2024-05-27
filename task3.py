orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

for name, item, quantity in orders:
    print(f'Order 1: {name} - {item}: quantity: {quantity}')
    for name, item, quantity in orders[1:]:
        print(f'Order 2: {name} - {item}: quantity: {quantity}')
    break