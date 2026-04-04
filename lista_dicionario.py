# Lista de produtos (nome, categoria, preço)
produtos = [
    ("Espada", "Armas", 150),
    ("Arco", "Armas", 120),
    ("Poção de Vida", "Consumíveis", 50),
    ("Poção de Mana", "Consumíveis", 60),
    ("Escudo", "Armas", 200),
    ("Comida", "Consumíveis", 30),
    ("Elmo", "Armaduras", 180),
    ("Peitoral", "Armaduras", 250)
]

# Função que cria o dicionário de categorias e calcula o valor total
def criar_dicionario(produtos):
    dicionario = {}   # Dicionário vazio para armazenar categorias e itens
    total = 0         # Variável para somar os preços

    # Percorre cada produto da lista
    for nome, categoria, preco in produtos:
        # Se a categoria ainda não existe no dicionário, cria uma lista vazia
        if categoria not in dicionario:
            dicionario[categoria] = []
        # Adiciona o nome do produto na lista da categoria correspondente
        dicionario[categoria].append((nome, preco))  # Guardamos nome e preço

        # Soma o preço do produto ao total geral
        total += preco

    # Retorna o dicionário de categorias e o valor total geral
    return dicionario, total

# Processamento: chama a função para organizar os dados
categorias, valor_total = criar_dicionario(produtos)

# Exibe o dicionário de categorias
print("Dicionário de Categorias:")
for cat, itens in categorias.items():
    nomes = [nome for nome, _ in itens]  # extrai apenas os nomes
    print(f"{cat}: {nomes}")

# Exibe o valor total em estoque
print(f"\nValor total em estoque: R$ {valor_total}")

# Loop até o usuário digitar "sair"
while True:
    categoria_usuario = input("\nDigite uma categoria (ou 'sair' para encerrar): ")

    if categoria_usuario.lower() == "sair":
        print("Encerrando programa...")
        break

    # Verifica se a categoria existe no dicionário
    if categoria_usuario in categorias:
        itens = categorias[categoria_usuario]
        nomes = [nome for nome, _ in itens]
        valor_categoria = sum(preco for _, preco in itens)
        print(f"Itens da categoria '{categoria_usuario}': {nomes}")
        print(f"Valor total da categoria '{categoria_usuario}': R$ {valor_categoria}")
    else:
        print("Categoria não encontrada.")