nome=input('')
fixo=float(input())
vendas=float(input())
comissao= (15 * vendas)/100
print("TOTAL = R$","%.2f"% (fixo+comissao))