entrada = list(map(float, input().split()))
valorPorLitro = entrada[:2]
kmPorLitro = entrada[2:]

rentabilidadeAlcool = kmPorLitro[0] / valorPorLitro[0]
rentabilidadeGasolina = kmPorLitro[1] / valorPorLitro[1]

if (rentabilidadeGasolina > rentabilidadeAlcool):
    print(f"G")
elif (rentabilidadeGasolina < rentabilidadeAlcool):
    print(f"A")
else:
    print(f"G")