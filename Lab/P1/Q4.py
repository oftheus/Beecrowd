N_a = int(input())
N_b = int(input())
N_c = int(input())

empresas = {
    'a' : N_a,
    'b' : N_b,
    'c' : N_c,
}

custos_em_a = empresas['b'] * 2 + empresas['c'] * 4
custos_em_b = empresas['a'] * 2 + empresas['c'] * 2
custos_em_c = empresas['b'] * 2 + empresas['a'] * 4

menor_custo = min([custos_em_a, custos_em_b, custos_em_c])

print(f"{menor_custo}")