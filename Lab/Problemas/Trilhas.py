class Trilha:

    def __init__(self, id, alturas):
        self.id = id
        self.alturas = alturas

    def Calcula_Esforco_De_Ida(self):
        esforco = 0
        
        for i in range(len(self.alturas) - 1):
            temp = self.alturas[i] - self.alturas[i + 1]
            esforco += temp*(-1) if temp < 0 else 0
        
        return esforco

    def Calcula_Esforco_De_Volta(self):
        esforco = 0
        volta = list(reversed(self.alturas))
        
        for i in range(len(volta) - 1):
            temp = volta[i] - volta[i + 1]
            esforco += temp*(-1) if temp < 0 else 0
        
        return esforco

    def Calcula_Menor_Esforco(self):
        esforco_ida = self.Calcula_Esforco_De_Ida()
        esfoco_volta = self.Calcula_Esforco_De_Volta()

        if (esforco_ida < esfoco_volta):
            return esforco_ida
        else:
            return esfoco_volta 


quantidade_de_trilhas = int(input())
trilhas = [None] * quantidade_de_trilhas


for i in range(quantidade_de_trilhas):    
    valores = list(map(int, input().split()))
    id = valores.pop(0)
    trilhas[i] = Trilha(i+1, valores)


menor_esforco = -1
identificador_trilha = -1

for trilha in trilhas:
    esforco = trilha.Calcula_Menor_Esforco()
    identificador = trilha.id

    if (esforco < menor_esforco or menor_esforco == -1):
        menor_esforco = esforco
        identificador_trilha = identificador
    elif(esforco == menor_esforco and identificador < identificador_trilha):
        menor_esforco = esforco
        identificador_trilha = identificador
    
print(f"{identificador_trilha}")
    

    
