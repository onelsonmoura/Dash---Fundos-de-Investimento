from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_tools import *

fundo = pd.read_parquet('./src/data/cad_fi.parquet')

app = Dash(__name__)

app.layout = html.Div([

    html.Div(className='wrapper', children=[

        html.Div(className='grid_info', children = [

            dash_tools.add_img(img_filename='drachma_logo.svg'),
            html.P(className= 'fund_name', id = 'nome_fundo'),
            html.P(className= 'fund_detail', id = 'sit_fundo'),

            dbc.Container(id = 'cards')
        ]),

        html.Div(className = 'grid_content', children = [
            
            html.Div(className='header', children=[
                dash_tools.profile(profile_pic='https://github.com/onelsonmoura.png', usermame='Nelson Moura'),
            ]),

            html.Hr(),

            html.Div(className= 'dropdown_line', children=[
                dash_tools.add_dropdown(title = 'Fundo', width = 400, list_itens = fundo['DENOM_SOCIAL'], value = fundo['DENOM_SOCIAL'][0], dropdown_id = 'fund_dropdown'),
                html.Div(id = 'fund_info'),
               
            ])
        ]),

    ])
])

@callback(
        
    Output('nome_fundo', 'children'), 
    Output('cards', 'children'), 
    Output('sit_fundo', 'children'),
    Input('fund_dropdown', 'value')
)

def refresh_output(nome_fundo):
    cards = []
    filtro = fundo[fundo['DENOM_SOCIAL'] == nome_fundo]

    cnpj_item = filtro['CNPJ_FUNDO'].item()
    classe_item = filtro['CLASSE'].item().upper()
    gestor_item = filtro['GESTOR'].item()
    sit = filtro['SIT'].item()

    itens = {
        'cnpj': ['receipt-2-1.svg', 'CNPJ', cnpj_item],
        'classe': ['bank.svg', 'CLASSE', classe_item],
        'gestor': ['people.svg', 'GESTORA', gestor_item]
    }

    def load_info(icon, title, item):

        card = html.Div(className='info', children=[
            dash_tools.add_img(f'icon/{icon}', class_name= 'img_info'),
            html.Div(className='text_info', children=[
                html.Strong(title.upper),
                html.Span(className= 'fund_detail', children= item)
            ]),
        ]),

        return card
    
    for item in itens:

        card = load_info(icon=itens[item][0], title=itens[item][1], item = itens[item][2])
        cards += [card]

    return nome_fundo, None, sit


if __name__ == '__main__':
    app.run(debug= True, port = 8050)