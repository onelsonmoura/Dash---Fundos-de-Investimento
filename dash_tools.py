from dash import html, dcc
import plotly.express as px
import pandas as pd

class dash_tools:

    def add_img(img_filename, class_name = None):

        image_path = f'./assets/image/{img_filename}'
        img = html.Img(className= f'{class_name}', src = image_path)

        return img
    
    def add_dropdown(title = None, list_itens = [], value = "", width = 100, dropdown_id = ''):

        dropdown = html.Div(className='dropdown', style= {'width': f'{width}px'}, children=[
                            html.P(children= title.upper()),
                            dcc.Dropdown(options= list_itens, value= value.upper(), multi= False, id = dropdown_id)
        ])

        return dropdown
    
    def profile(profile_pic, usermame):
        
        profile = html.Div(className= 'welcome', children = [
            html.Img(src = profile_pic),
            html.Div(className= 'welcomeInfo', children = [
                html.Span('Welcome back, '),
                html.Strong(f'{usermame}')
            ])
        ])

        return profile
    
    def load_series(arquivo, coluna):
        
        df = pd.read_parquet(f'./src/data/{arquivo}')
        series = df[coluna]

        return series


