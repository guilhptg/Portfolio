from pydoc import classname

from dash import html, dcc
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Diretório do script atual
pasta_assets = os.path.join(BASE_DIR, 'assets')


arquivos = os.listdir(pasta_assets)
print(arquivos)
# TODO uma lógica para o dono da página adicionar e remover imagens e projetos. Editar a pagina como um todo
layout = html.Div([
    html.H1("Marketing Digital"),
    html.Div([
        html.H2("Marketing Digital - WebDesign"),
        html.Div([
            html.Img(src='/assets/2.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/3.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/5.jpg', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 1
        ], classname='image-gallery'),
    ]),
    html.Div([
        html.H2("WebDesign"),
        html.Div([
            html.Img(src='/assets/4.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/8.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/10.jpg', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
        html.H2("Qr Code"),
        html.Div([
            html.Img(src='/assets/qrlabor.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor1.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor2.png', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
    ]),
    # Adicione mais álbuns conforme necessário
])
