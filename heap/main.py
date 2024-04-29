class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        # Adiciona o valor ao final da lista.
        self.heap.append(valor)
        # Move o novo valor para a posição correta no heap.
        self._subir_no_heap(len(self.heap) - 1)

    def remover(self):
        if self.heap:
            # Remove e retorna o valor mínimo (o primeiro elemento).
            if len(self.heap) == 1:
                return self.heap.pop()
            # Troca o primeiro e o último elementos.
            self._trocar(0, len(self.heap) - 1)
            # Remove o último elemento (anteriormente o mínimo).
            minimo = self.heap.pop()
            # Move o novo primeiro elemento para a posição correta no heap.
            self._descer_no_heap(0)
            return minimo
        else:
            raise IndexError("O heap está vazio")

    def obter_minimo(self):
        if self.heap:
            # Retorna o valor mínimo (o primeiro elemento).
            return self.heap[0]
        else:
            raise IndexError("O heap está vazio")

    def tamanho(self):
        return len(self.heap)

    def _subir_no_heap(self, indice):
        pai_indice = (indice - 1) // 2
        if pai_indice >= 0 and self.heap[indice] < self.heap[pai_indice]:
            # Se o valor for menor que seu pai, troca-os e continua recursivamente.
            self._trocar(indice, pai_indice)
            self._subir_no_heap(pai_indice)

    def _descer_no_heap(self, indice):
        filho_esquerdo_indice = 2 * indice + 1
        filho_direito_indice = 2 * indice + 2
        menor = indice

        # Encontra o índice do menor filho, se houver.
        if filho_esquerdo_indice < len(self.heap) and self.heap[filho_esquerdo_indice] < self.heap[menor]:
            menor = filho_esquerdo_indice
        if filho_direito_indice < len(self.heap) and self.heap[filho_direito_indice] < self.heap[menor]:
            menor = filho_direito_indice

        if menor != indice:
            # Se o valor for maior que o menor filho, troca-os e continua recursivamente.
            self._trocar(indice, menor)
            self._descer_no_heap(menor)

    def _trocar(self, i, j):
        # Função auxiliar para trocar dois elementos na lista.
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Exemplo de uso
min_heap = MinHeap()
min_heap.inserir(3)
min_heap.inserir(1)
min_heap.inserir(4)
min_heap.inserir(2)

print("Tamanho do heap:", min_heap.tamanho())  # Saída: 4
print("Elemento mínimo:", min_heap.obter_minimo())  # Saída: 1

while min_heap.tamanho() > 0:
    print(min_heap.remover())  # Saída: 1 2 3 4
