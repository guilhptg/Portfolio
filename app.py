import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Inicializar o app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout principal com o Localização para roteamento e o Div que conterá as páginas
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link('Home', href='/', className='nav-link')),
            dbc.NavItem(dcc.Link('Python Projets', href='/python-projects', className='nav-link')),
            dbc.NavItem(dcc.Link('Web Design', href='/web-design', className='nav-link')),
            dbc.NavItem(dcc.Link('Marketing Digital', href='/marketing-digital', className='nav-link')),
            dbc.NavItem(dcc.Link('Comunicação Visual', href='/comunicacao-visual', className='nav-link')),
            dbc.NavItem(dcc.Link('Contato', href='contato', className='nav-link')),
        ],
        brand='• Guilherme Portugal',
        brand_href='/',
        color='darkblue',
        dark=True,
    ),
    html.Div(id='page-content')
])

# Callback para atualizar o conteúdo da página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/python-projects':
        from pages import python_projects
        return python_projects.layout
    elif pathname == '/web-design':
        from pages import web_design
        return web_design.layout
    elif pathname == '/marketing-digital':
        from pages import marketing_digital
        return marketing_digital.layout
    elif pathname == '/comunicacao-visual':
        from pages import comunicacao_visual
        return comunicacao_visual.layout
    elif pathname == '/contato':
        from pages import contato
        return contato.layout
    elif pathname == '/certificados':
        from pages import certificados
        return certificados.layout
    else:
        from pages import home
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
