# por tentativa
# n = 0 --- d = 4  (quadrado exato)
# n = 1 --- d = 9  (quadrado exato)
# n = 2 --- d = 25 (quadrado exato)
# n = 3 --- erro!  (ñ sei)
# n = 4 --- erro!  (ñ sei)

# relação entre entradas e a raiz das saidas
# n = 0 --- d = 4 --- r = 2  
# n = 1 --- d = 9 --- r = 3  --- cresce +1 em relação ao anterior (inicia com 1 não tem como fazer dobro do R anterior)
# n = 2 --- d = 25--- r = 5  --- cresce +2 em relação ao anterior (dobro da diferença entre os R anteriores) dif = (1)*2 = 2
# n = 3 --- erro!  (ñ sei)   --- (dobro da diferença entre os R anteriores) = 4 portanto dif = (2)*2 = 4 | r = (4) + 5 = 9  e d = 81 (quadrado exato)
# n = 4 --- erro!  (ñ sei)   --- (dobro da diferença entre os R anteriores) = 8 portanto dif = (4)*2 = 8 | r = (9) + 8 = 17 e d = 289 (quadrado exato)

# aplicando o algoritimo anterior :  
# n = 0 --- d = 4    --- r = 2
# n = 1 --- d = 9    --- r = 3  (+1)  --> 2^0
# n = 2 --- d = 25   --- r = 5  (+2)  --> 2^1
# n = 3 --- d = 81   --- r = 9  (+4)  --> 2^2
# n = 4 --- d = 289  --- r = 17 (+8)  --> 2^3
# n = 5 --- d = 1089 --- r = 33 (+16) --> 2^4
#                                     Também pode ser descrito por qudrado da entrada anterior                                        
# portanto a saída é a soma do da raiz do resultado anterior com o quadrado da entrada
# deve começar em 1 pois não tem relação quando a entrada é igual a 0

entrada = int(input())

contador_de_testes = 1

while (entrada != -1):       
    
    r = 2
    for i in range(entrada):        
        r += 2**i 
    
    d = r*r

    print(f"Teste {contador_de_testes}")
    print(f"{d}")
    print()
    contador_de_testes += 1
    entrada = int(input())