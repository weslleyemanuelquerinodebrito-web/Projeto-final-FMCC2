"""
Função que verifica se um elemento é gerador de um grupo.
"""

def eh_gerador(grupo, elemento, ordem):
 
    # o Grupo é o conjunto de elementos que serão inseridos na função
    # o elemento é o que será testado se é capaz de gerar todos os outros elementos do grupo.
    # a ordem é o número de elementos no grupo.
        

    a = 0  
    # a variavel "a" é um contador que vai contar quantos elementos distintos  o elemento escolhido gerou. 

    gerados = []  
    # Lista que vai armazenando os resultados (elemento^exp mod ordem)

    for exp in range(1, ordem + 1):
        # loop que percorre os expoentes de 1 até a ordem do grupo, para testar se o elemento escolhido gera os outros elementos do grupo.

        resultado = pow(elemento, exp, ordem)  
        # Calcula elemento^exp e depois tira o módulo pela ordem do grupo.

        if resultado not in gerados:
            # Se o resultado não estiver na lista, ele adicionará e somará +1 no contador "a".

            gerados.append(resultado)
            a += 1

    if a == len(grupo):
        return True
    return False
    # Se o valor de "a" for igual ao tamanho do grupo, significa que o elemento testado é gerador, pois gerou todos os elementos do grupo, retornando true.
    #  Caso contrário, ele não é gerador retornando false.


"""
Função que verifica se o grupo é cíclico, ou seja, se existe pelo menos
um elemento capaz de gerar todos os outros elementos do grupo.
"""
def eh_ciclico(grupo, ordem):
    #O grupo a ser testado é o mesmo que foi testado na função eh_gerador, e a ordem é o número de elementos no grupo.

    for num in grupo:
        # loop que percorre cada elemento do grupo, testando um por um como possível gerador, testando se cada elemento é gerador apartir da função eh_gerador.
        # Caso exista algum elemento que seja gerador, a função retornará True e o próprio elemento gerador encontrado.
        # Caso contrário, retornará False e None, pois não há elemento que seja gerador.

        if eh_gerador(grupo, num, ordem):
            return True, num

    return False, None
