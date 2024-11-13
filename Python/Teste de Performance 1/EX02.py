numeroMin = int(input("Digite um número de minutos: "))

horas = numeroMin // 60
minutos = numeroMin % 60
print(f"{numeroMin} minutos é igual a {horas} horas e {minutos} minutos.")

horasInput = int(input("Digite um número de horas: "))
minutosInput = int(input("Digite um número de minutos: "))

minutosTotais = horasInput * 60 + minutosInput

print(f"{horasInput} horas e {minutosInput} minutos é igual a {minutosTotais} minutos.")