from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
from dash import dash_table

home_layout = html.Div(children=[
    dcc.Dropdown(id='input_data',
                 style={'display': 'none'}),
    html.Div([
        html.H1(children="Welcome to the Olympics broadcasting analytic dashboard!"),
        html.Div([
            html.P([html.H3('Data Table', style={"color": "black", }),
                    dcc.Markdown('''
                    The below data is a snapshot of the csv.
                    ''', style={'margin-top': '10px',
                                'color': 'black',
                                'line-height': '1'}),
                    html.Hr(),
                    dbc.Spinner(html.Div(id='data_table',
                                         style={'height': '700px'}), color='blue')                
                    
                    ])
        ], className='table_bg twelve columns')
    ], className='table_row row')
],className="alls")

@app.callback(Output("data_table", "children"),
              Input("input_data", "value"))

def update_table(data):
    df = pd.read_csv('dataset/olympics_data.csv')
    return dbc.Table.from_dataframe(df, striped=False, bordered=False, hover=True)
