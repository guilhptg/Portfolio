from dash import html, dcc

layout = html.Div([
    html.H1("Trabalhos Recentes"),
    html.Ul([
        html.Li(dcc.Link('Trabalho 1: Descrição do trabalho 1', href='/trabalho1')),
        html.Li(dcc.Link('Trabalho 2: Descrição do trabalho 2', href='/trabalho2')),
        # Adicione mais itens conforme necessário
    ]),
])
