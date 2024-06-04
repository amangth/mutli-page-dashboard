from dash import html
import plotly.express as px
import pandas as pd
from dash import dcc
from dash.dependencies import Input, Output

from app import app

####################### DATASET #############################
df = pd.read_csv('dataset/olympics_data.csv')

#######################  bar CHART #############################
def create_bar_chart(x_axis="gender", y_axis="age"):
    return px.bar(data_frame=df, x=x_axis, y=y_axis, height=600)

#################### Options #############################
columns = ["age", "number_of_visits", "total_view_hours", "main_interest_event", "second_interest_event", "web_browser", "device_streamed_on","gender","time_of_event"]

x_axis = dcc.Dropdown(id="x_axis", options=columns, value="gender", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="age", clearable=False)

rlp_layout = html.Div(children=[
    html.H1(children="This is a relationships page" ),
      html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="Bar")

],className='table_row row')


####################### CALLBACKS ###############################
@app.callback(Output("Bar", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_bar_chart(x_axis, y_axis):
    return create_bar_chart(x_axis, y_axis)