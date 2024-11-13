from dash import html, dcc

layout = html.Div([
        html.H2("Aplicação de adesivo vinílico"),
        html.H4('Serviços prestados para empresas privadas no DF e entorno.'),
        html.Div([
            html.Img(src='/assets/qrlabor.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor1.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor2.png', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
    ]),
    # Adicione mais álbuns conforme necessário

# Se a pessoa tiver interesse, faz um cadastro para entrar em contato. Propor trabalho, tirar duvidas ou elogiar. Campo para CONTATO
