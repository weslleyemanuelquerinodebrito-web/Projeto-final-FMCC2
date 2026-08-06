
def eh_gerador(grupo, elemento, ordem):
    """
    Verifica se 'elemento' é um gerador do grupo, ou seja, se suas
    potências sucessivas (elemento^1, elemento^2, ...) produzem
    TODOS os elementos do grupo.
    """

    a = 0  
    # 'a' é um contador: guarda quantos elementos DISTINTOS
    # já foram gerados pelas potências do 'elemento' até agora.

    gerados = []  
    # Lista que vai armazenando os resultados (elemento^exp mod ordem)
    # já encontrados, para não contar valores repetidos.

    for exp in range(1, ordem + 1):
        # Percorre os expoentes de 1 até 'ordem' (o tamanho/ordem do grupo).
        # Precisamos testar até 'ordem' potências porque, no pior caso,
        # um gerador só completa o ciclo completo na última potência.

        resultado = pow(elemento, exp, ordem)  
        # Calcula elemento^exp e depois tira o módulo pela ordem do grupo.
        # Isso simula a operação do grupo multiplicativo módulo 'ordem'.

        if resultado not in gerados:
            # Só contamos o resultado se ele ainda não tiver aparecido antes.
            # Isso evita contar valores repetidos mais de uma vez.

            gerados.append(resultado)
            # Adiciona o novo valor à lista de valores já gerados.

            a += 1
            # Incrementa o contador, pois encontramos mais um elemento novo.

    return a == len(grupo)
    # Se a quantidade de elementos distintos gerados (a) for igual
    # ao tamanho total do grupo, significa que o 'elemento' conseguiu
    # gerar TODOS os elementos do grupo -> ele é um gerador.
    # Caso contrário, ele só gerou uma parte (um subgrupo menor) -> não é gerador.


def eh_ciclico(grupo, ordem):
    """
    Verifica se o grupo é cíclico, ou seja, se existe pelo menos
    UM elemento capaz de gerar todos os outros elementos do grupo.
    """

    for num in grupo:
        # Percorre cada elemento do grupo, testando um por um
        # como possível gerador.

        if eh_gerador(grupo, num, ordem):
            # Chama a função anterior para verificar se 'num' é gerador.

            return True, num
            # Se encontrarmos QUALQUER elemento que seja gerador,
            # já podemos afirmar que o grupo é cíclico.
            # Retornamos True e o próprio elemento gerador encontrado.

    return False, None
    # Se o loop terminar e nenhum elemento tiver sido gerador,
    # então o grupo NÃO é cíclico.
    # Retornamos False e None (não há gerador).


# --- Exemplo de uso: (Z/7Z)*, grupo multiplicativo módulo 7 ---
if __name__ == "__main__":
    # Esse bloco só roda quando o arquivo é executado diretamente
    # (não roda se o arquivo for importado como módulo em outro script).

    n = 7
    # Define a ordem do grupo (número de elementos / módulo usado).

    grupo = [1, 2, 3, 4, 5, 6]
    # Define os elementos do grupo (Z/7Z)*, ou seja, os números de 1 a 6,
    # que são os elementos invertíveis módulo 7 (exclui o 0).

    ciclico, gerador = eh_ciclico(grupo, n)
    # Chama a função principal para verificar se o grupo é cíclico,
    # e guarda o resultado (True/False) e o gerador encontrado (ou None).

    print(f"É cíclico? {ciclico}, gerador encontrado: {gerador}")
    # Exibe o resultado final na tela.