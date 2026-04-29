grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

class Cola:
    def __init__(self):
        self.elementos = []

    def enqueue(self, valor):
        self.elementos.append(valor)

    def dequeue(self):
        return self.elementos.pop(0)

    def esta_vacia(self):
        return len(self.elementos) == 0

    def __repr__(self):
        return str(self.elementos)


def bfs(grafo):
    visitados = []
    cola = Cola()

    print(f"Cola inicial:     {cola}")
    print(f"Visitados inicial: {visitados}\n")

    for inicio in grafo:
        if inicio not in visitados:
            visitados.append(inicio)
            cola.enqueue(inicio)

            print(f"Enqueue '{inicio}':")
            print(f"Cola:      {cola}")
            print(f"Visitados: {visitados}\n")

            while not cola.esta_vacia():
                nodo = cola.dequeue()
                print(f"Visitando: {nodo}")

                for vecino in grafo[nodo]:
                    if vecino not in visitados:
                        visitados.append(vecino)
                        cola.enqueue(vecino)

                print(f"Cola:      {cola}")
                print(f"Visitados: {visitados}\n")

    print(f"Recorrido final BFS: {visitados}")

bfs(grafo)