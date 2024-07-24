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
            dbc.NavItem(dcc.Link('Álbuns de Fotos', href='/albums', className='nav-link'))
        ],
        brand='Dashboard',
        brand_href='/',
        color='primary',
        dark=True,
    ),
    html.Div(id='page-content')
])

# Callback para atualizar o conteúdo da página
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/albums':
        from pages import albums
        return albums.layout
    else:
        from pages import home
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
