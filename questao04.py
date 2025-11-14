print("\n" + "=" * 60)
print("               CALCULADORA DE PREÇO TOTAL")
print("=" * 60)

# Entrada dinâmica
nome_produto = input("\nDigite o nome do produto: ")

preco_unitario = input("Digite o preço unitário (R$): ").replace(",", ".")
preco_unitario = float(preco_unitario)

quantidade = int(input("Digite a quantidade: "))

# Cálculo
preco_total = preco_unitario * quantidade

# Resultado
print("\n" + "-" * 60)
print(f"Produto.................: {nome_produto}")
print(f"Preço unitário..........: R$ {preco_unitario}")
print(f"Quantidade..............: {quantidade}")
print("-" * 60)
print(f"Preço total da compra...: R$ {preco_total}")
print("-" * 60)
print("Operação finalizada com sucesso.")
print("=" * 60 + "\n")

input("Pressione ENTER para sair...")
