from heapq import heappop, heappush
'Importa as funções heappop e heappush do módulo heapq, que são utilizadas para criar e "gerenciar uma fila de prioridade".'


def astar(comeco, destino, graph):
    fronteira = []
    'lista q armazena os nós a serem explorados;'
    heappush(fronteira, (0, comeco))
    'Adiciona na fronteira uma uma tupla contendo a distância inicial, que é zero, e o nó de partida.'
    visitado = set()
    'conjunto q armazenar os nós já visitados'
    caminho_percorrido = {}
    'Utilizado para armazenar o caminho percorrido até o momento.'
    custo_caminho_percorrido = {comeco: 0}
    'Associa a cada nó o "custo do caminho percorrido até ele". Neste caso, o custo do caminho até o nó de partida é zero.'
    custo_estimado_destino = {comeco: heuristic(comeco, destino)}
    'Cria um dicionário chamado custo_estimado_destino que associa a cada nó o valor da função de "custo estimado para chegar ao destino". '
    'Neste caso, a função de custo é a heurística que retorna a distância de Manhattan entre o nó e o destino.'
    
    while fronteira:
        atual = heappop(fronteira)[1]
        '"heappop = Remove" o primeiro elemento da fronteira e atribui o segundo elemento da tupla (que representa o nó) à variável "atual".'
        if atual == destino:
            return recostruir_caminho(caminho_percorrido, comeco, destino)
        
        visitado.add(atual)
        
        for vizinho in graph[atual]:
            'Para cada vizinho do nó atual:'
            tentative_custo_caminho_percorrido = custo_caminho_percorrido[atual] + 1
            'Calcula o custo atual do caminho até o vizinho.'
            if vizinho in visitado and tentative_custo_caminho_percorrido >= custo_caminho_percorrido.get(vizinho, float('inf')):
                'Se o vizinho já foi visitado e o custo atual é maior ou igual ao custo anterior, continua para o próximo vizinho.'
                continue
            if tentative_custo_caminho_percorrido < custo_caminho_percorrido.get(vizinho, float('inf')):
                'Se o custo atual é menor que o custo anterior do vizinho:'
                caminho_percorrido[vizinho] = atual
                'Atualiza o dicionário caminho_percorrido com o nó anterior.'
                custo_caminho_percorrido[vizinho] = tentative_custo_caminho_percorrido
                'Atualiza o dicionário custo_caminho_percorrido com o novo custo estimado'
                custo_estimado_destino[vizinho] = tentative_custo_caminho_percorrido + heuristic(vizinho, destino)
                'atualiza o dicionário custo_estimado_destino com o novo custo estimado mais a heurística de estimativa de custo para chegar a destino a partir de vizinho.'
                'é atualizado com o custo atual mais o custo estimado para chegar ao destino'
                if vizinho not in visitado:
                    heappush(fronteira, (custo_estimado_destino[vizinho], vizinho))
                    'Se o vizinho ainda não foi visitado, ele é adicionado à fronteira.'
                    'se vizinho ainda não foi visitado, ele é adicionado à fronteira com o novo custo estimado custo_estimado_destino[vizinho] como sua prioridade.'
                    
    return None


def recostruir_caminho(caminho_percorrido, comeco, destino):
    caminho = [destino]
    while caminho[-1] != comeco:
        caminho.append(caminho_percorrido[caminho[-1]])
        'A função procura o nó anterior no caminho percorrido do nó inicial até o nó de destino.'
    caminho.reverse()
    return caminho


def heuristic(no, destino):
    return abs(no[0] - destino[0]) + abs(no[1] - destino[1])


graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(0, 2), (1, 1), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(1, 1), (2, 0), (2, 2)],
    (2, 2): [(1, 2), (2, 1)]
}


comeco = (0, 0)
destino = (2, 1)


caminho = astar(comeco, destino, graph)


print(caminho)



