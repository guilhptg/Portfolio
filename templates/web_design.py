from dash import html

layout = html.Div([
    html.H1("Web Design"),
    html.P("Edições e montagens feitas por mim (Guilherme Portugal), para um empresa de joias dentais."),
    html.Div([
        html.H2("Labor ICE Grillz"),
        html.Div([
            html.Img(src='/assets/marketing_digital/2.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/marketing_digital/3.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/marketing_digital/5.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/marketing_digital/4.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/marketing_digital/8.jpg', style={'width': '30%', 'margin': '10px'}),
            html.Img(src='/assets/marketing_digital/10.jpg', style={'width': '30%', 'margin': '10px'}),
            # Adicione mais fotos para o Trabalho 1
        ]),
    ]),
    # Adicione mais conteúdo conforme necessário
])
