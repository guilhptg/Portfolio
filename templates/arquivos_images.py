# import os
#
#
# '''Comunicação Visual - Paths and Archives'''
# base_path_comunicacao_visual = '/home/usuario/Documentos/GitHub/Portfolio/assets'
#
# file_path_comunicacao_visual = os.listdir(base_path_comunicacao_visual)
#
# lista_trabalhos = [trabalho for trabalho in file_path_comunicacao_visual]
#
# for trabalho in lista_trabalhos:
#     file_path_comunicacao_visual = os.listdir(os.path.join(base_path_comunicacao_visual + trabalho))
#
#
# print(lista_trabalhos)
#
# print(file_path_comunicacao_visual)
import os

'''Comunicação Visual - Paths and Archives'''
base_path_comunicacao_visual = '/home/usuario/Documentos/GitHub/Portfolio/assets/comunicacao_visual'

# Dicionário para armazenar os trabalhos por pasta
lista_trabalhos = {}

# Itera pelas subpastas no diretório base
for pasta in os.listdir(base_path_comunicacao_visual):
    # Caminho completo para a subpasta
    pasta_path = os.path.join(base_path_comunicacao_visual, pasta)

    # Verifica se é um diretório antes de tentar listar os arquivos
    if os.path.isdir(pasta_path):
        # Lista apenas os arquivos com extensões de imagem
        arquivos = [
            f"/assets/comunicacao_visual/{pasta}/{arquivo}"  # Caminho para uso no Dash
            for arquivo in os.listdir(pasta_path)
            if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
        ]
        # Adiciona ao dicionário
        lista_trabalhos[pasta] = arquivos

# Exibe os resultados no console para depuração
print("Lista de Trabalhos:")
for pasta, arquivos in lista_trabalhos.items():
    print(f"Pasta: {pasta}, Arquivos: {arquivos}")
