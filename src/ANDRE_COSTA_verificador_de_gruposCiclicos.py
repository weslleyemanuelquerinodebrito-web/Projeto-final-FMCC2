"""
Função que verifica se um elemento é gerador de um grupo.
"""

def eh_gerador(tabela, elemento):
 
    # a tabela é o conjunto de elementos que serão testados na função, será tratada no formato de matriz em python
    # o elemento é o que será testado se é capaz de gerar todos os outros elementos do grupo.
        
    a = 0  
    # a variavel "a" é um contador que vai contar quantos elementos distintos  o elemento escolhido gerou. 

    gerados = []  
    # Lista que vai armazenando os resultados (elemento^exp mod ordem)

    atual = elemento
    # 'atual' guarda o resultado da potência corrente do elemento.
 
    for _ in range(len(tabela)):
        # loop que percorre até o len(tabela) que é o tamanho do grupo, pois um gerador percorre todos elementos ate o fim do tamanho de seu grupo.

        if atual not in gerados:
            # Se o elemento atual não estiver na lista, ele adicionará e somará +1 no contador "a".

            gerados.append(atual)
            a += 1
         
        atual = tabela[atual][elemento]
        #É feito um cruzamento na tabela para descobrir o resultado do numero "atual" com "elemento", equivalente á atual= atual * elemento

             
    if a == len(tabela):
        return True
    return False
    # Se o valor de "a" for igual ao tamanho do grupo, significa que o elemento testado é gerador, pois gerou todos os elementos do grupo, retornando true.
    #  Caso contrário, ele não é gerador retornando false.

"""
Função que verifica se o grupo da tabela é cíclico, ou seja, se existe pelo menos
um elemento capaz de gerar todos os outros elementos do grupo.
"""
def eh_ciclico(tabela, identidade):
    #A tabela a ser testada é a mesma que foi testada na função eh_gerador.

    n = len(tabela)
    # Tamanho do grupo = número de elementos = número de linhas da tabela.

    for num in range(n):
       # loop que percorre cada elemento do grupo de 0 ate n-1
           # Serão testados um  elemento por um como possível gerador, testando se cada elemento é gerador apartir da função eh_gerador.
           # Caso exista algum elemento que seja gerador, a função retornará True e o próprio elemento gerador encontrado.
           # Caso contrário, retornará False e None, pois não há elemento que seja gerador.

        if eh_gerador(tabela, num, identidade):
        # Se nenhum elemento gerar o grupo todo, ele não é cíclico.  

            return True, num
    return False, None


