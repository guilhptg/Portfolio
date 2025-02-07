from dash import html, dcc

layout = html.Div([
        html.H2("Contato"),
        html.H4('Complete o formulário com seus dadaos e nos envie com sua necessidade. Que no prazo mais curto responderemos'),
        html.Div([
            html.Img(src='/assets/qrlabor.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor1.png', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/qrlabor2.png', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 2
        ]),
    ]), html.Fieldset([
    html.H3('Ola, se tem interesse em contatar ou contrar algum serviço. Deixe seus dados que entraremos em contato.')
]),
    # Adicione mais álbuns conforme necessário

# Se a pessoa tiver interesse, faz um cadastro para entrar em contato. Propor trabalho, tirar duvidas ou elogiar. Campo para CONTATO

