import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import home, relationships, distribution,five_number, choropleth


url_content_layout = html.Div(children=[
    dcc.Location(id="url",refresh=False),
    html.Div(id="output-div"),
    html.Div(
        [
            html.Div([
                html.Div([
                    html.H5("Olympics Dashboard", style={'color': 'white', 'margin-top': '10px'}),
                ], className='image_title')
            ], className="sidebar-header"),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-house"),
                        html.Span("Home", style={'margin-top': '3px'})], className='link_element')],
                        href="/",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Relationships", style={'margin-top': '3px'})], className='link_element')],
                        href="/relationships",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-database"),
                        html.Span("Distribution", style={'margin-top': '3px'})], className='link_element')],
                        href="/distribution",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-circle-info"),
                        html.Span("Choropleth", style={'margin-top': '3px'})], className='link_element')],
                        href="/choropleth",
                        active="exact",
                        className="pe-3"
                    ),
                      dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-circle-info"),
                        html.Span("Five Number Summary", style={'margin-top': '3px'})], className='link_element')],
                        href="/five_number",
                        active="exact",
                        className="pe-3"
                    ),
                
                ],
                vertical=True,
                pills=True,
            ),
        ],
        id="bg_id",
        className="sidebar",
    )
  
],className="alls")

app.layout = url_content_layout



@app.callback(Output(component_id="output-div",component_property="children"),Input(component_id="url",component_property="pathname"))
def update_output_div(pathname):
    if pathname == "/relationships":
        return  relationships.rlp_layout
    elif pathname == "/distribution":
        return distribution.dist_layout
    elif pathname == "/five_number":
        return five_number.five_layout
    elif pathname == "/choropleth":
        return choropleth.chr_layout
    else:
        return home.home_layout


if __name__ == "__main__":
    app.run_server(debug=True)
    