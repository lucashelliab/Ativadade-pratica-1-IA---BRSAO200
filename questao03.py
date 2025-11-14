import time

print("\n" + "=" * 55)
print("              CALCULADORA DE VOLUME")
print("=" * 55)

time.sleep(0.6)
print("\nPreparando dados da caixa...")
time.sleep(0.8)

comprimento = 12
largura = 14
altura = 20

time.sleep(0.6)
print(f"Comprimento: {comprimento} cm")
time.sleep(0.5)
print(f"Largura:     {largura} cm")
time.sleep(0.5)
print(f"Altura:      {altura} cm")

time.sleep(0.8)
print("\nCalculando volume", end="")
for _ in range(3):
    time.sleep(0.4)
    print(".", end="")
time.sleep(0.5)

volume = comprimento * largura * altura

print("\n")
print("-" * 55)
print(f"Volume total da caixa: {volume} cm³")
print("-" * 55)
print("Cálculo concluído com sucesso.")
print("=" * 55 + "\n")
