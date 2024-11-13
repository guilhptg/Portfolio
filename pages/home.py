from dash import html, dcc, Input
import dash_bootstrap_components as dbc

layout = html.Div([
    html.H1("Somethings about me"),
    html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dcc.Link('Python Projets', href='/python-projects', className='nav-link'), ),
                dbc.NavItem(dcc.Link('Web Design', href='/web-design', className='nav-link')),
                dbc.NavItem(dcc.Link('Marketing Digital', href='/marketing-digital', className='nav-link')),
                dbc.NavItem(dcc.Link('Comunicação Visual', href='/comunicacao-visual', className='nav-link')),
                dbc.NavItem(dcc.Link('Certificados', href='/certificados', className='nav-link')),
            ],
            color='black',
            dark=True,
        )
    ]),
    html.Div([
    html.Img(src='/assets/eu_1.jpeg', style={'width': '30%', 'margin': '10px'})]),
    html.P('Me chamo Victor Guilherme Soares Portugal, mais conhecido como Guilherme ou Portuga. '
           'Tenho 26 anos e no ano de 2024 eu iniciei minha jornada na programação, '
           'de cara me apaixonei por python e desde então venho aprimorando meus projetos'),
        ]),

