class BuscadorCamino:
    def __init__(self, grafo):
        self.grafo = grafo
        self.camino = []

    def buscar(self, inicio, valor_buscar):
        """
        Función recursiva para buscar en profundidad.
        Debe recibir el valor inicial y el objetivo.
        Devuelve el valor a buscar o None si no lo encuentra.
        """
        self.camino.append(inicio)
        if inicio == valor_buscar:
            return valor_buscar

        resultado = None  # Inicializa resultado como None

        for k, v in self.grafo.items():
            if v == inicio:
                resultado = self.buscar(k, valor_buscar)

            if resultado:
                return resultado

        self.camino.pop()  # Si no se encontró el valor en este nivel, elimina el último nodo del camino
        return resultado  # Devuelve resultado en lugar de None

if __name__ == "__main__":
    valores = {
        "b1": "B",
        "b2": "B",
        "b3": "b2",
        "b4": "b2",
        "b5": "b4",
        "b6": "b4",
        "A": "b6"
    }

    origen = input("Ingresa un nodo de origen: ")
    destino = input("Ingresa un nodo de destino: ")

    buscador = BuscadorCamino(valores)
    resultado = buscador.buscar(origen, destino)

    if resultado:
        print(buscador.camino)
    else:
        print("No encontrado")
