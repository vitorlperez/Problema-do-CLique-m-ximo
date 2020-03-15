def Clique(grafo, vertice_base):
    C =[]
    for i in range(len(grafo[vertice_base])):
        if grafo[vertice_base][i] == 1:
            C.append(i)          
    for i in C:
        linha = grafo[i]
        j = 0
        while j < len(C):
            if len(C) != 0:
                if i != C[j]:
                    if linha[C[j]] != 1:
                        C.pop(j)
                    else:
                        j += 1
                else:
                    j+=1
            else:
                j += 1
    return len(C)+1

def CliqueInv(grafo, vertice_base):
    C =[]
    for i in range(len(grafo[vertice_base])):
        if grafo[vertice_base][i] == 1:
            C.append(i)
    C = C[::-1]        
    for i in C:
        linha = grafo[i]
        j = 0
        while j < len(C):
            if len(C) != 0:
                if i != C[j]:
                    if linha[C[j]] != 1:
                        C.pop(j)
                    else:
                        j += 1
                else:
                    j+=1
            else:
                j += 1
    return len(C)+1

num_arestas = int(input())

grafo = []
for i in range(num_arestas-1):
	linha = [0 for j in range(num_arestas-1)]
	grafo.append(linha)

for i in range(num_arestas):
	ligacao = str(input())
	ligacao = ligacao.split()
	grafo[int(ligacao[0])-1][int(ligacao[1])-1] = 1
	grafo[int(ligacao[1])-1][int(ligacao[0])-1] = 1

cliques = []
for i in range(num_arestas-1):
    aux = Clique(grafo, i)
    cliques.append(aux)
for i in range(num_arestas-1):
    aux = CliqueInv(grafo, i)
    cliques.append(aux)
print(max(cliques))
