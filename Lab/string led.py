visitados = []
def dfs(no,grafo):
    
    node = [] #node - os outros nos que esse no vai visitar
    for c in range(len(grafo[no])):
        
        node.append(grafo[no][c])
        
    #print(mrc)    
    for c in range(len(node)):
        if node[c] not in visitados:
            visitados.append(node[c])
            dfs(node[c], grafo)

nseg, nlin = map(int, input().split())

grafo = {}

for c in range(nlin):
    
    a,b = map(int, input().split())
    
    if a in grafo:
        
        if b not in grafo[a]:
            
            grafo[a].append(b)        
    else:
        grafo[a] = []
        grafo[a].append(b)
        
    if b in grafo:
        
        if a not in grafo[b]:
            
            grafo[b].append(a)    
    else:
        grafo[b] = []
        grafo[b].append(a)

dfs(1, grafo)

if nseg==len(visitados):
    print("COMPLETO")

else:
    print("INCOMPLETO")