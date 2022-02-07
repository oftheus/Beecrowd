def DefineVencedorPelaOrdemDeChegada(listaDeChegada):
    for index, ingresso in enumerate(listaDeChegada):
        if (index+1) == ingresso:
            return ingresso


contadorDeTestes = 1
numeroDeIngressosVendidos = int(input())

while numeroDeIngressosVendidos != 0:    
    ordemDeChegada = list(map(int, input().split()))
    print(f"Teste {contadorDeTestes}")
    vencedor = DefineVencedorPelaOrdemDeChegada(ordemDeChegada)
    print(f"{vencedor}")
    numeroDeIngressosVendidos = int(input())
    contadorDeTestes += 1
    print()


