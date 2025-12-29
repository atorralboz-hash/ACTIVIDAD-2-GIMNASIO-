"""
programa calculo imc preguntando peso y altura
"""

# pedir el pedo y la altura
print("introduce tu peso en kg")
peso = float(input())
#peso_num = float(peso)

altura = float(input("introduce tu altura en m"))

# calculo del IMC
# imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print(imc)
