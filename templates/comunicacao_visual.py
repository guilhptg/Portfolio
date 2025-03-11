from dash import html, dcc

layout = html.Div([
    html.H2("Aplicação de adesivo vinílico"),
    html.H6("Serviços prestados para empresas privadas no DF e entorno."),

    # Álbum de fotos do trabalho
    html.H3('Óticas Requinte - Adesivo'),
    html.Div([
        html.Img(src='/assets/comunicacao_visual/adesivo_requinte/consultorio_processo_0.jpeg', style={'width': '30%', 'margin': '10px'}),
        # Adicione mais imagens aqui
    ], className='image-gallery', style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),

    # Álbum de fotos do trabalho
    html.H2("Vídeo de demonstração"),
    html.Video(
        controls=True,  # Habilita os controles de reprodução (play, pause, volume etc.)
        src="/assets/videos/demonstracao.mp4",  # Caminho para o arquivo de vídeo
        style={'width': '80%', 'margin': '20px auto', 'display': 'block'}  # Estilização
    ),

    html.H2('Rodoviária Alexissania'),
    html.H3('Troca de letreiro e adesivação de uma placa de acrílico para a empresa Guanabara'),
    html.H3('Antes'),
    html.Div([
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_2.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_3.jpeg', style={'width': '30%', 'margin': '10px'}),
        # Adicione mais imagens aqui
    ], className='image-gallery', style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),

    # Álbum de fotos do trabalho
    html.H3('Depois'),
    html.Div([
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_5.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_4.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_7.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_9.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_8.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviairia_alexissania/rodoviaria_alexissania_11.jpeg', style={'width': '30%', 'margin': '10px'}),
        # Adicione mais imagens aqui
    ], className='image-gallery',  style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),

    # Álbum de fotos do trabalho
    html.H2('Terminal de Vendas de Passagem UTB - Rodoviária do Plano Piloto - Brasilia'),
    html.H3('Adesivo Lateral e Letreiro Luminoso'),
    html.Div([
        html.Img(src='assets/comunicacao_visual/rodoviaria plano piloto/adesivo_rodoviaria_plano_piloto.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviaria plano piloto/adesivo_rodoviaria_plano_piloto_2.jpeg', style={'width': '30%', 'margin': '10px'}),
        html.Img(src='assets/comunicacao_visual/rodoviaria plano piloto/adesivo_rodoviaria_plano_piloto_4.jpeg', style={'width': '30%', 'margin': '10px'}),
        # Adicione mais imagens aqui
    ], className='image-gallery', style={'display': 'flex', 'flex-wrap': 'wrap', 'justify-content': 'center'}),


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
        ], className='image-gallery', style={'max-width': '500px', 'margin': '20px auto'})
    ])
])