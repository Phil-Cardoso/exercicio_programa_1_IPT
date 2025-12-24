# Exercício-Programa 1

## Implementação da Árvore Rubro-Negra em Python

---

### Autor

Phillip da Silva Cardoso

---

## 1. Descrição do Projeto

Este projeto consiste na implementação de uma **Árvore Rubro-Negra**, uma estrutura de dados do tipo árvore binária de busca balanceada, conforme proposto no Exercício-Programa 1 da disciplina **Estruturas de Dados e Análise de Algoritmos**.

A árvore rubro-negra mantém o balanceamento automaticamente após operações de **inserção** e **remoção**, garantindo que a altura da árvore permaneça em **O(log n)**. Para isso, são aplicadas **rotações** e **recolorações** sempre que alguma das propriedades rubro-negras é violada.

O programa permite:

* Inserir elementos
* Buscar elementos
* Remover elementos
* Visualizar a árvore em formato bidimensional após cada inserção e remoção

---

## 2. Propriedades da Árvore Rubro-Negra

A implementação respeita rigorosamente as seguintes propriedades:

1. Cada nó é vermelho ou preto
2. A raiz da árvore é sempre preta
3. Todas as folhas (NIL) são pretas
4. Se um nó é vermelho, então seus filhos são pretos
5. Todo caminho da raiz até uma folha contém o mesmo número de nós pretos

---

## 3. Linguagem e Ambiente

* Linguagem: **Python 3**
* Ambiente recomendado:

  * Windows 10
  * Visual Studio Code
* O código utiliza apenas recursos nativos da linguagem Python, não sendo necessárias bibliotecas externas.

---

## 4. Como Executar o Programa

1. Certifique-se de ter o Python 3 instalado.
2. Salve o arquivo principal como, por exemplo:

```
main.py
```

3. Execute o programa pelo terminal ou prompt de comando:

```
python main.py
```

---

## 5. Menu do Programa

Ao executar o programa, será exibido o seguinte menu:

```
1 - Inserir
2 - Buscar
3 - Remover
4 - Mostrar árvore
0 - Sair
```

* Após **inserir** ou **remover** um elemento, a árvore é automaticamente exibida em formato bidimensional.
* A opção “Mostrar árvore” permite visualizar o estado atual da árvore a qualquer momento.

---

## 6. Exemplos de Testes

### 6.1 Inserções

Inserir os valores na seguinte ordem:

```
10, 20, 30
```

Resultado esperado:

* Ocorre uma rotação simples para manter o balanceamento.

---

Inserir os valores:

```
10, 5, 15, 1
```

Resultado esperado:

* Ocorre recoloração dos nós, sem rotação.

---

Inserir os valores:

```
10, 5, 8
```

Resultado esperado:

* Ocorre uma rotação dupla (esquerda-direita).

---

### 6.2 Remoções

Após inserir os valores:

```
20, 15, 25, 10, 5, 1, 30, 22, 27
```

Realizar as remoções:

```
1
5
15
```

Resultado esperado:

* A árvore permanece balanceada após cada remoção, com correção de cores e rotações quando necessário.

---

### 6.3 Buscas

Buscar um elemento existente:

```
Buscar: 22
Resultado: Elemento encontrado
```

Buscar um elemento inexistente:

```
Buscar: 99
Resultado: Elemento não encontrado
```

---

## 7. Visualização da Árvore

A árvore é exibida em formato bidimensional no terminal, onde:

* Cada nó mostra seu valor e sua cor (VERMELHO ou PRETO)
* A estrutura hierárquica facilita a visualização do balanceamento
* A árvore é impressa automaticamente após cada inserção e remoção