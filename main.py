class No:
    """
    Representa um nó da árvore rubro-negra.

    Cada nó possui:
    - uma chave (valor armazenado),
    - uma cor (VERMELHO ou PRETO),
    - referências para o nó pai,
      filho esquerdo e filho direito.
    """

    VERMELHO = "R"
    PRETO = "B"

    def __init__(self, chave):
        """
        Inicializa um novo nó da árvore.

        Parâmetros:
        chave (int): valor a ser armazenado no nó
        """
        self.chave = chave
        self.cor = No.VERMELHO
        self.esquerda = None
        self.direita = None
        self.pai = None


class ArvoreRubroNegra:
    """
    Implementa uma árvore rubro-negra, uma árvore binária de busca balanceada.

    Permite operações de inserção, busca e remoção,
    garantindo que as propriedades rubro-negras sejam mantidas.
    """

    def __init__(self):
        """
        Inicializa a árvore rubro-negra.

        Cria o nó NULO, utilizado para representar folhas,
        e define a raiz inicial da árvore.
        """
        self.NULO = No(None)
        self.NULO.cor = No.PRETO
        self.raiz = self.NULO

    # ROTAÇÕES
    def rotacao_esquerda(self, x):
        """
        Realiza uma rotação simples à esquerda em torno do nó x.

        Essa rotação é utilizada para restaurar o balanceamento
        da árvore após inserções ou remoções.
        """
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.NULO:
            y.esquerda.pai = x

        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y

        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, x):
        """
        Realiza uma rotação simples à direita em torno do nó x.

        Essa rotação é utilizada para restaurar o balanceamento
        da árvore após inserções ou remoções.
        """
        y = x.esquerda
        x.esquerda = y.direita
        if y.direita != self.NULO:
            y.direita.pai = x

        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.direita:
            x.pai.direita = y
        else:
            x.pai.esquerda = y

        y.direita = x
        x.pai = y

    # INSERÇÃO
    def inserir(self, chave):
        """
        Insere um novo elemento na árvore rubro-negra.

        O nó é inicialmente inserido como em uma árvore binária
        de busca comum e, em seguida, são feitas correções para
        garantir as propriedades rubro-negras.
        """
        novo_no = No(chave)
        novo_no.esquerda = self.NULO
        novo_no.direita = self.NULO

        pai = None
        atual = self.raiz

        while atual != self.NULO:
            pai = atual
            if novo_no.chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo_no.pai = pai
        if pai is None:
            self.raiz = novo_no
        elif novo_no.chave < pai.chave:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no

        novo_no.cor = No.VERMELHO
        self.corrigir_insercao(novo_no)

        self.imprimir_arvore(self.raiz)

    def corrigir_insercao(self, k):
        """
        Corrige possíveis violações das propriedades rubro-negras
        causadas pela inserção de um novo nó.

        Aplica recolorações e rotações conforme o caso analisado.
        """
        while k.pai and k.pai.cor == No.VERMELHO:
            if k.pai == k.pai.pai.esquerda:
                tio = k.pai.pai.direita
                if tio.cor == No.VERMELHO:
                    k.pai.cor = No.PRETO
                    tio.cor = No.PRETO
                    k.pai.pai.cor = No.VERMELHO
                    k = k.pai.pai
                else:
                    if k == k.pai.direita:
                        k = k.pai
                        self.rotacao_esquerda(k)
                    k.pai.cor = No.PRETO
                    k.pai.pai.cor = No.VERMELHO
                    self.rotacao_direita(k.pai.pai)
            else:
                tio = k.pai.pai.esquerda
                if tio.cor == No.VERMELHO:
                    k.pai.cor = No.PRETO
                    tio.cor = No.PRETO
                    k.pai.pai.cor = No.VERMELHO
                    k = k.pai.pai
                else:
                    if k == k.pai.esquerda:
                        k = k.pai
                        self.rotacao_direita(k)
                    k.pai.cor = No.PRETO
                    k.pai.pai.cor = No.VERMELHO
                    self.rotacao_esquerda(k.pai.pai)

        self.raiz.cor = No.PRETO

    # BUSCA
    def buscar(self, chave):
        """
        Busca um elemento na árvore rubro-negra.

        Retorna o nó correspondente à chave, caso exista,
        ou o nó NULO caso não seja encontrado.
        """
        atual = self.raiz
        while atual != self.NULO and atual.chave != chave:
            if chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return atual

    # REMOÇÃO
    def transplantar(self, u, v):
        """
        Substitui o subárvore enraizada em u pela subárvore
        enraizada em v.
        """
        if u.pai is None:
            self.raiz = v
        elif u == u.pai.esquerda:
            u.pai.esquerda = v
        else:
            u.pai.direita = v
        v.pai = u.pai

    def minimo(self, no):
        """
        Retorna o nó com o menor valor em uma subárvore.
        """
        while no.esquerda != self.NULO:
            no = no.esquerda
        return no

    def remover(self, chave):
        """
        Remove um elemento da árvore rubro-negra.

        Após a remoção, realiza as correções necessárias
        para manter as propriedades da árvore.
        """
        z = self.buscar(chave)
        if z == self.NULO:
            print("Elemento não encontrado.")
            return

        y = z
        cor_original = y.cor

        if z.esquerda == self.NULO:
            x = z.direita
            self.transplantar(z, z.direita)
        elif z.direita == self.NULO:
            x = z.esquerda
            self.transplantar(z, z.esquerda)
        else:
            y = self.minimo(z.direita)
            cor_original = y.cor
            x = y.direita
            if y.pai == z:
                x.pai = y
            else:
                self.transplantar(y, y.direita)
                y.direita = z.direita
                y.direita.pai = y

            self.transplantar(z, y)
            y.esquerda = z.esquerda
            y.esquerda.pai = y
            y.cor = z.cor

        if cor_original == No.PRETO:
            self.corrigir_remocao(x)

        self.imprimir_arvore(self.raiz)

    def corrigir_remocao(self, x):
        """
        Corrige possíveis violações das propriedades rubro-negras
        após a remoção de um nó.

        Trata casos de duplo-preto utilizando rotações e recolorações.
        """
        while x != self.raiz and x.cor == No.PRETO:
            if x == x.pai.esquerda:
                w = x.pai.direita
                if w.cor == No.VERMELHO:
                    w.cor = No.PRETO
                    x.pai.cor = No.VERMELHO
                    self.rotacao_esquerda(x.pai)
                    w = x.pai.direita
                if w.esquerda.cor == No.PRETO and w.direita.cor == No.PRETO:
                    w.cor = No.VERMELHO
                    x = x.pai
                else:
                    if w.direita.cor == No.PRETO:
                        w.esquerda.cor = No.PRETO
                        w.cor = No.VERMELHO
                        self.rotacao_direita(w)
                        w = x.pai.direita
                    w.cor = x.pai.cor
                    x.pai.cor = No.PRETO
                    w.direita.cor = No.PRETO
                    self.rotacao_esquerda(x.pai)
                    x = self.raiz
            else:
                w = x.pai.esquerda
                if w.cor == No.VERMELHO:
                    w.cor = No.PRETO
                    x.pai.cor = No.VERMELHO
                    self.rotacao_direita(x.pai)
                    w = x.pai.esquerda
                if w.direita.cor == No.PRETO and w.esquerda.cor == No.PRETO:
                    w.cor = No.VERMELHO
                    x = x.pai
                else:
                    if w.esquerda.cor == No.PRETO:
                        w.direita.cor = No.PRETO
                        w.cor = No.VERMELHO
                        self.rotacao_esquerda(w)
                        w = x.pai.esquerda
                    w.cor = x.pai.cor
                    x.pai.cor = No.PRETO
                    w.esquerda.cor = No.PRETO
                    self.rotacao_direita(x.pai)
                    x = self.raiz
        x.cor = No.PRETO

    # IMPRESSÃO BIDIMENSIONAL
    def imprimir_arvore(self, no, indent="", ultimo=True):
        """
        Imprime a árvore em formato bidimensional no terminal,
        exibindo a hierarquia e a cor de cada nó.
        """
        if no != self.NULO:
            print(indent, end="")
            if ultimo:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            cor = "VERMELHO" if no.cor == No.VERMELHO else "PRETO"
            print(f"{no.chave} ({cor})")
            self.imprimir_arvore(no.esquerda, indent, False)
            self.imprimir_arvore(no.direita, indent, True)


if __name__ == "__main__":
    arvore = ArvoreRubroNegra()

    while True:
        print("\n1 - Inserir")
        print("2 - Buscar")
        print("3 - Remover")
        print("4 - Mostrar árvore")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Valor a inserir: "))
            arvore.inserir(valor)

        elif opcao == "2":
            valor = int(input("Valor a buscar: "))
            resultado = arvore.buscar(valor)
            if resultado != arvore.NULO:
                print(f"Elemento {valor} encontrado.")
            else:
                print("Elemento não encontrado.")

        elif opcao == "3":
            valor = int(input("Valor a remover: "))
            arvore.remover(valor)

        elif opcao == "4":
            arvore.imprimir_arvore(arvore.raiz)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")



# insercao: 20, 15, 25, 10, 5, 1, 30, 22, 27
# remocao: 1,5,15
# busca: 22, 99
