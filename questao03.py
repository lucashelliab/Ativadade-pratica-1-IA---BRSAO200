print("\n" + "=" * 60)
print("                 CALCULADORA DE VOLUME")
print("=" * 60)

# Entrada dos valores
comprimento = float(input("Digite o COMPRIMENTO da caixa (cm): "))
largura = float(input("Digite a LARGURA da caixa (cm): "))
altura = float(input("Digite a ALTURA da caixa (cm): "))

# Cálculo
volume = comprimento * largura * altura

# Resultado
print("\n" + "=" * 60)
print("                     RESULTADO FINAL")
print("=" * 60)
print(f"Comprimento: {comprimento} cm")
print(f"Largura:     {largura} cm")
print(f"Altura:      {altura} cm")
print("-" * 60)
print(f"Volume total da caixa: {volume} cm³")
print("-" * 60)
print("Cálculo concluído com sucesso!")
print("=" * 60 + "\n")

input("Pressione ENTER para sair...")
