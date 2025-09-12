productos = [("Manzana",1.2),("Banana",0.5),("Cereza",2.35)]

print(f"{'Producto':<10}|{'Precio':>7}")
print("-" * 20)
for i , j in productos:


    print(f"{i:<10}|{j:>7.2f}")