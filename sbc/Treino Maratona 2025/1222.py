while True:
    try:
        N, L, C = map(int, input().split())
        conto = input().split()

        linhas_usadas = 0
        caracteres_na_linha = 0
        paginas_usadas = 1

        for palavra in conto:
            if caracteres_na_linha + len(palavra) <= C:
                caracteres_na_linha += len(palavra) + 1
            else:
                linhas_usadas += 1
                if linhas_usadas == L:
                    paginas_usadas += 1
                    linhas_usadas = 0
                caracteres_na_linha = len(palavra) + 1

        print(paginas_usadas)
    except EOFError:
        break