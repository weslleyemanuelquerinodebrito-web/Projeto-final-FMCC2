""" 
Função que checa o axíoma do fechamento para um conjunto
"""
def checar_fechamento(conjunto, tabela):
    """  
    Lista que contém tuplas, cada tupla indica uma dupla de elementos operados entre sí que falharam o axíoma
    """
    elementos_falhos = []

    """ 
    Loop que percorre cada elemento operado da tabela e verifica se ele está no conjunto original
    """
    for i in range(tabela.length()):
        for j in range(tabela[i].length()):
            if tabela[i][j] not in conjunto:
                elementos_falhos.append((tabela[i], tabela[j]))

    """
    Se a lista de elementos falhos estiver vazia, retorna True, indicando que o axioma é 
    verdadeiro para o conjunto, caso contrário, retorna a lista de tuplas com os elementos falhos.
    """
    if not elementos_falhos:
        return True
    else:
        return elementos_falhos

"""  
Função que checa se o conjunto possui elemento neutro.
"""
def checar_elemento_neutro(conjunto, tabela):

    """ 
    Loop for que percorre cada linha da matriz de operações, caso a linha seja exatamente igual o conjunto,
    significa que o elemento correspondente àquela linha é o elemento neutro do conjunto, então, retorna o
    elemento neutro através do índice encontrado no loop, caso não encontre nenhuma linha correspondene ao conjunto
    original, retorna False.
    """
    for i in range(tabela.length()):
        if tabela[i] == conjunto:
            return conjunto[i]

    return False

""" 
Função que checa se cada elemento do conjunto possui um inverso, o elemento neutro anteriormente encontrado
é passado como parâmetro pois será útil para agilizar o processo.
"""
def checar_inversos(conjunto, tabela, elemento_neutro):
    """  
    Lista que representa cada elemento que não possui inverso na operação indicada
    """
    falhos = []

    """ 
    Loop que percorre todas as linhas da matriz, utilizando o elemento neutro como parâmetro, caso o elemento neutro
    seja encontrado naquela linha, significa que o elemento correspondente daquela linha possui um inverso da operação
    em uma das colunas.

    Caso o elemento neutro não seja encontrado, significa que o elemento daquela linha não possui inverso, sendo adicionado na 
    lista de elementos que falham no axíoma.
    """
    for i in range(tabela.length()):
        if elemento_neutro not in tabela[i]:
            falhos.append(conjunto[i])

    """ 
    Se a lista de elementos falhos não estiver vazia, retorna ela, mostrando todos os elementos que falham no axíoma, caso contrário,
    retorna True, indiciando que o axíoma funciona para o conjunto. 
    """
    if falhos:
        return falhos
    else:
        return True
