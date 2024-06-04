from dash import html
from dash import dcc,callback,dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import statistics

from app import app
df = pd.read_csv('dataset/olympics_data.csv')

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}


five_layout = html.Div(children=[
    html.H1(children="This is a five number summary page"),
    
    dcc.Tabs(id="tab-inline", value='tab-1', children=[
        dcc.Tab(label='Averages', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Max', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Min', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Sum', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Count', value='tab-5', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),

    html.Div(id='tabs-content-inline-3')
    
    
    
    ],className='table_row row')


@callback(Output('tabs-content-inline-3', 'children'), Input('tab-inline', 'value'))

def render_content(tab):
    if tab == 'tab-1':   
        return html.Div([
        # html.H3('Tab content 1'), 
         html.Div([
        dcc.Graph(id='our_graph')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options=[
                    {'label': 'Average Visits ', 'value': 'number_of_visits'},
                    {'label': 'Average Time', 'value': 'total_view_hours'},
                
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='total_view_hours',                     #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),
       

    ])

    elif tab == 'tab-2':
        return html.Div([
        # html.H3('Tab content 1'), 
         html.Div([
        dcc.Graph(id='graph1')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='dropdown1',
            options=[
                    {'label': 'Max Visits ', 'value': 'number_of_visits', },
                    {'label': 'Max Time', 'value': 'total_view_hours'},
                
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='total_view_hours',                     #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),
       

    ])
    elif tab == 'tab-3':return html.Div([
        # html.H3('Tab content 1'), 
         html.Div([
        dcc.Graph(id='graph2')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='dropdown2',
            options=[
                    {'label': 'Min Visits ', 'value': 'number_of_visits'},
                    {'label': 'Min Time', 'value': 'total_view_hours'},
                
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='total_view_hours',                     #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),
       

    ])
    elif tab == 'tab-4':
        return html.Div([
        # html.H3('Tab content 1'), 
         html.Div([
        dcc.Graph(id='graph3')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='dropdown3',
            options=[
                    {'label': 'Sum of Visits ', 'value': 'number_of_visits'},
                    {'label': 'Sum of Time', 'value': 'total_view_hours'},
                
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='total_view_hours',                     #dropdown value selected automatically when page loads
            disabled=False,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),
       

    ])
    elif tab == 'tab-5':return html.Div([
        # html.H3('Tab content 1'), 
         html.Div([
        dcc.Graph(id='graph4')
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='dropdown4',
            options=[
                    {'label': 'Count  Visits ', 'value': 'number_of_visits'},
                    {'label': 'Count Time', 'value': 'total_view_hours'},
                
            ],
            optionHeight=35,                    #height/space between dropdown options
            value='total_view_hours',                     #dropdown value selected automatically when page loads
            disabled=True,                     #disable dropdown value selection
            multi=False,                        #allow multiple dropdown values to be selected
            searchable=True,                    #allow user-searching of dropdown values
            search_value='',                    #remembers the value searched in dropdown
            placeholder='Please select...',     #gray, default text shown when no option is selected
            clearable=True,                     #allow user to removes the selected value
            style={'width':"100%"},             #use dictionary to define CSS styles of your dropdown
            className='select_box',           #activate separate CSS document in assets folder
            # persistence=True,                 #remembers dropdown value. Used with persistence_type
            # persistence_type='memory'         #remembers dropdown value selected until...
            ),                                  #'memory': browser tab is refreshed
                                                #'session': browser tab is closed
                                                #'local': browser cookies are deleted
    ],className='three columns'),
       

    ]) 



@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)
def update_graph(column_chosen):
    fig = px.histogram(df, x= 'gender', y=column_chosen ,histfunc='avg')
    fig.update_layout(bargap=0.2)
    return fig


@app.callback(
    Output(component_id='graph1', component_property='figure'),
    [Input(component_id='dropdown1', component_property='value')]
)

def update_graph1(column_chosen):
    fig = px.histogram(df, x= 'gender', y=column_chosen ,histfunc='max')
    fig.update_layout(bargap=0.2)
    return fig

@app.callback(
    Output(component_id='graph2', component_property='figure'),
    [Input(component_id='dropdown2', component_property='value')]
)

def update_graph1(column_chosen):
    fig = px.histogram(df, x= 'gender', y=column_chosen ,histfunc='min')
    fig.update_layout(bargap=0.2)
    return fig

@app.callback(
    Output(component_id='graph3', component_property='figure'),
    [Input(component_id='dropdown3', component_property='value')]
)

def update_graph1(column_chosen):
    fig = px.histogram(df, x= 'gender', y=column_chosen ,histfunc='sum')
    fig.update_layout(bargap=0.2)
    return fig

@app.callback(
    Output(component_id='graph4', component_property='figure'),
    [Input(component_id='dropdown4', component_property='value')]
)

def update_graph1(column_chosen):
    fig = px.histogram(df, x= 'gender', y=column_chosen ,histfunc='count')
    fig.update_layout(bargap=0.2)
    return fig
