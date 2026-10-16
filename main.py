import itertools
import random

def gerar_jogos_megasena():
    print("=== GERADOR MEGA-SENA POR LINHAS (TESTE ONLINE) ===\n")
    
    # 1. Grupo Base de Dezenas
    texto_dezenas = input("Digite o seu grupo base de dezenas (separadas por espaço): ")
    try:
        texto_limpo = texto_dezenas.replace(",", " ")
        dezenas_usuario = sorted(list(set(int(x) for x in texto_limpo.split())))
        
        for d in dezenas_usuario:
            if d < 1 or d > 60:
                print(f"Erro: A dezena {d} é inválida (deve ser entre 1 e 60).")
                return
        
        if len(dezenas_usuario) < 6:
            print("Erro: Insira pelo menos 6 dezenas no grupo base!")
            return
    except ValueError:
        print("Erro: Formato inválido nas dezenas.")
        return

    # 2. Padrão de Linhas (L1 a L6)
    print("\nDefina o padrão de dezenas por linha (As 6 linhas devem somar exatamente 6):")
    padrao = []
    nomes_linhas = ["L1 (01-10)", "L2 (11-20)", "L3 (21-30)", "L4 (31-40)", "L5 (41-50)", "L6 (51-60)"]
    
    for nome in nomes_linhas:
        val = int(input(f"Quantas dezenas quer na {nome}?: "))
        padrao.append(val)
    
    if sum(padrao) != 6:
        print(f"\nErro: A soma do padrão deve ser exatamente 6 (A sua soma atual é: {sum(padrao)}).")
        return

    # 3. Quantidade de Jogos
    qtd_desejada = int(input("\nQuantos jogos deseja extrair?: "))
    if qtd_desejada <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return

    # 4. Separar dezenas por linha
    linhas_usuario = [[] for _ in range(6)]
    for d in dezenas_usuario:
        idx_l = (d - 1) // 10
        if idx_l < 6:
            linhas_usuario[idx_l].append(d)

    # Validar disponibilidade
    for i in range(6):
        if len(linhas_usuario[i]) < padrao[i]:
            print(f"Erro: A Linha {i+1} exige {padrao[i]} dezenas, mas você só forneceu {len(linhas_usuario[i])} no grupo base.")
            return

    # 5. Cruzamento combinatório
    opcoes_por_linha = []
    for i in range(6):
        k = padrao[i]
        if k == 0:
            opcoes_por_linha.append([()])
        else:
            opcoes_por_linha.append(list(itertools.combinations(linhas_usuario[i], k)))

    jogos_encontrados = []
    for combinacao_linhas in itertools.product(*opcoes_por_linha):
        jogo = []
        for tupla_linha in combinacao_linhas:
            jogo.extend(tupla_linha)
        if len(jogo) == 6:
            jogos_encontrados.append(tuple(sorted(jogo)))

    total_possivel = len(jogos_encontrados)
    if total_possivel == 0:
        print("\nNenhum jogo encontrado para este padrão com as dezenas fornecidas.")
        return

    # 6. Seleção e Exibição
    if qtd_desejada >= total_possivel:
        jogos_selecionados = jogos_encontrados
        aviso = f"(Total máximo disponível: {total_possivel} jogos)."
    else:
        jogos_selecionados = random.sample(jogos_encontrados, qtd_desejada)
        aviso = f"(Mostrando {qtd_desejada} de {total_possivel} jogos possíveis)."

    print(f"\n--- RESULTADOS ---")
    print(f"Padrão escolhido: {padrao} | {aviso}\n")
    
    for idx, jogo in enumerate(jogos_selecionados, 1):
        jogo_formatado = " - ".join(f"{num:02d}" for num in jogo)
        print(f"Jogo {idx:03d}: {jogo_formatado}")

# Executar a função
gerar_jogos_megasena()