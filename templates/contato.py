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
    html.Fieldset([
        html.H3('Ola, se tem interesse em contatar ou contrar algum serviço. Deixe seus dados que entraremos em contato.')
        ]),

    # Campo de contato
    html.Div([
        html.H4("Entre em contato conosco!"),
        html.Div([
            html.Label("Nome:"),
            dcc.Input(type="text", placeholder="Seu nome", style={'margin-bottom': '10px', 'width': '100%'}),
            html.Label("E-mail:"),
            dcc.Input(type="email", placeholder="Seu e-mail", style={'margin-bottom': '10px', 'width': '100%'}),
            html.Label("Mensagem:"),
            dcc.Textarea(placeholder="Escreva sua mensagem aqui...",
                         style={'width': '100%', 'height': '100px', 'margin-bottom': '10px'}),
            html.Button("Enviar", style={'padding': '10px 20px', 'background-color': '#007bff', 'color': 'white',
                                         'border': 'none'})
        ], style={'max-width': '500px', 'margin': '20px auto'})
    ]),
]),
    # Adicione mais álbuns conforme necessário

# Se a pessoa tiver interesse, faz um cadastro para entrar em contato. Propor trabalho, tirar duvidas ou elogiar. Campo para CONTATO

