productos = [("Laptop", 950.75), ("Mouse", 25.5), ("Teclado", 49.99)]

print(f"{'Producto':<10} | {'Precio':>8}")

print("-"*22)

for i,j in productos:
    print(f"{i:<10} | {j:>8.2f}")