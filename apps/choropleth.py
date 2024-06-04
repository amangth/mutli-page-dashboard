from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from plotly.data import gapminder
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import pandas as pd

from app import app

df = pd.read_csv('dataset/olympics_data2.csv', dtype={"code": str}) 



chr_layout = html.Div(children=[
    html.H1(children="This is a choropleth page, for average age by sporting event per country"),
    html.P("Select a feature for display:"),
    dcc.RadioItems(
        id='feature', 
        options=[{'label':'All', 'value':'All'},
                 {'label':'Football', 'value':'Football'},
                 {'label':'Hockey', 'value':'Hockey'},
                 {'label':'Volleyball', 'value':'Volleyball'},
                ],
        value="All",
        inline=True
    ),
    dcc.Graph(id="graph", figure={}),
], className='table_row row')


@app.callback(
    Output("graph", "figure"), 
[Input('feature', 'value')])

def display_choropleth(selected):
    df = pd.read_csv('dataset/olympics_data2.csv', dtype={"code": str})  
    if selected=='All':
        df = df
    else:
        df = df[df['main_interest_event']==selected]

    fig = go.Figure(data=go.Choropleth(         
    locations = df['country-origin'],     
    locationmode = 'country names',                          
    z = df['age'],
    text = df['country-origin'],
    colorscale = 'Blues', 
    autocolorscale=False, 
    reversescale= False, 
    marker_line_color='darkgray',      
    colorbar_title = 'age'                              
    ))
       
    fig.update_layout(
    title_text='Olympic Viewers ',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),) 
    return fig 