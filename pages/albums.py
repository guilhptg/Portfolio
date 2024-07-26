from dash import html, dcc

layout = html.Div([
    html.H1("Álbuns de Fotos"),
    html.Div([
        html.H2("Trabalho 1"),
        html.Div([
            html.Img(src='/assets/2.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/3.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/5.jpg', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 1
        ]),
    ]),
    html.Div([
        html.H2("Trabalho 2"),
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
