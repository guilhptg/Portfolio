from dash import html, dcc

layout = html.Div([
            html.H2('Emissor de Notas'),
            html.P('Automação feita para emitir notas através de um banco de dados .XMLX. Podendo assim emitir 30 notas em 12 segundos.'
                   'A aplicação conta com um tranformador de .CSV para .XMLX e visse versa usando o pandas'),
            html.H2('E-commerce with Django'),
            html.Div([
                html.Img(src='/assets/projetos_python/projetest.png', style={'width': '30%', 'margin': '10px'}),
                html.Img(src='/assets/projetos_python/web_scrapping.png', style={'width': '30%', 'margin': '10px'}),
                # html.Img(src='/assets/projetos_python/5.jpg', style={'width': '30%', 'margin': '10px'}),
            ], className='image-gallery')
        ]),

    # Adicione mais álbuns conforme necessário

# Se a pessoa tiver interesse, faz um cadastro para entrar em contato. Propor trabalho, tirar duvidas ou elogiar. Campo para CONTATO
