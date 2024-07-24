from dash import html

layout = html.Div([
    html.H1("Trabalhos Recentes"),
    html.Ul([
        html.Li("Trabalho 1: Descrição do trabalho 1"),
        html.Li("Trabalho 2: Descrição do trabalho 2"),
        # Adicione mais itens conforme necessário
    ]),
])
