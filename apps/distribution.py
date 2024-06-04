from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



from app import app

df = pd.read_csv('dataset/olympics_data.csv')
def create_distribution(col_name="age"):
    return px.histogram(data_frame=df, x=col_name, height=600)

columns = ["age", "main_interest_event", "second_interest_event", "device_streamed_on", "language", "web_browser"]
dd = dcc.Dropdown(id="dist_column", options=columns, value="age", clearable=False)

dist_layout = html.Div(children=[
    html.H1(children="This is a distribution page"),
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")     
    ],className='table_row row')



@app.callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)