from dash import html, dcc

layout = html.Div([
        html.H2("Cerfiticações e Competênciasexi"),
        html.P('Complete o formulário com seus dadaos e nos envie com sua necessidade. Que no prazo mais curto responderemos'),
        html.H3('Leaning and Produtivity'),
        html.Div([
            html.Img(src='/assets/learning_and_productivity.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/laerning_and_produtivity_2.png', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
        html.H3('Curriculo Python'),
        html.Div([
            html.Img(src='/assets/python0.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/python1.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/python2.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/python3.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/python4.png', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
    ]),
    # Adicione mais álbuns conforme necessário

# Se a pessoa tiver interesse, faz um cadastro para entrar em contato. Propor trabalho, tirar duvidas ou elogiar. Campo para CONTATO

