import time

print("\n" + "=" * 60)
print("               CALCULADORA DE PREÇO TOTAL")
print("=" * 60)

time.sleep(0.7)
print("\nCarregando informações do produto...")
time.sleep(1)

nome_produto = "Mouse Gamer RGB"
preco_unitario = 89.90
quantidade = 2

print(f"\nProduto.................: {nome_produto}")
time.sleep(0.5)
print(f"Preço unitário..........: R$ {preco_unitario}")
time.sleep(0.5)
print(f"Quantidade..............: {quantidade}")

time.sleep(0.8)
print("\nProcessando", end="")
for _ in range(3):
    time.sleep(0.4)
    print(".", end="")
time.sleep(0.4)

preco_total = preco_unitario * quantidade

print("\n")
print("-" * 60)
print(f"Preço total da compra...: R$ {preco_total}")
print("-" * 60)
print("Operação finalizada com sucesso.")
print("=" * 60 + "\n")
