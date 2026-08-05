"""
Função que calcula a ordem de cada elemento do conjunto.
"""
def calcular_ordens(conjunto, tabela, elemento_neutro):
    """
    a ordem de um elemento a é o menor número de vezes que se precisa
    operar a consigo mesmo (a * a * a * ...) até chegar no elemento neutro.
    rcebe o elemento neutro já calculado pela função (checar_elemento_neutro), 
    pra não precisar recalcular.
    """
    n = len(conjunto)
    ordens = {}

    """
    loop que percorre cada elemento do conjunto e vai acumulando
    a operação dele consigo mesmo até bater no elemento neutro,
    contando quantas operações foram necessárias por meio de um contador
    """

    for elem in conjunto:
        atual = elem
        contador = 1

        while atual != elemento_neutro:
            i = conjunto.index(atual)
            j = conjunto.index(elem)
            atual = tabela[i][j]
            contador += 1

            """
            trava de segurança: se passar da ordem do conjunto sem
            achar o neutro, alguma coisa está errada (a tabela não
            forma um grupo de fato, ou fechamento ou a associatividade falharam).
            """
            if contador > n:
                raise ValueError(f"Elemento {elem} não retorna ao neutro dentro de {n} passos")

        ordens[elem] = contador

    return ordens


"""
função que formata o resultado de calcular_ordens em texto,
mostrando a ordem de cada elemento do conjunto.
"""
def formata_ordens(ordens):
    """
    Recebe o dicionário produzido por calcular_ordens
    e monta uma lista de linhas de texto, uma pra cada elemento,
    juntando tudo no final em uma unica string.
    """
    linhas = ["Ordem de cada elemento:"]
    for elem, ordem in ordens.items():
        linhas.append(f"  ordem({elem}) = {ordem}")
    return "\n".join(linhas)


# testezinho rapido
if __name__ == "__main__":
    print("=== teste: Z4, soma módulo 4 ===")
    conjunto = [0, 1, 2, 3]
    n = 4
    tabela = [[(a + b) % n for b in range(n)] for a in range(n)]
    ordens = calcular_ordens(conjunto, tabela, elemento_neutro=0)
    print(formata_ordens(ordens))
    # esperado: ordem(0)=1, ordem(1)=4, ordem(2)=2, ordem(3)=4
