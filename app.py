from dash import dcc
from dash import html
from dash.dependencies import Input
from dash.dependencies import Output
from main import app
import dash_bootstrap_components as dbc
# Connect to your app pages
from app import textbox, upload, contact

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "color": "#00488E", #2c65fb
    "background-color": "#cbddfc"}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem"
}

sidebar = html.Div([  # NOQA E501
    html.Img(src='./assets/federal_logo_small.png',  # NOQA E501
             style={"max-width": "210px", "height": "auto", "margin": "0.27rem"}),  # NOQA E501
    html.Hr(),
    html.H4("ChatGPT BOT", className="display-6",
            style={'textAlign': 'left'}),
    html.P("NLP LLM Tool", className="lead",
           style={'textAlign': 'left', "height": "10px"}),
    html.P("Version 0.0", className="lead", style={'textAlign': 'left'}),
    dbc.Nav([dbc.NavLink("User Input", href="/app/textbox", className="page-link",  # NOQA E501
                    style={"color": "#f5f0ed", "background-color": "#2c65fb"}),  # NOQA E501
        html.Br(style={"margin-top": "2.5px"}),  # NOQA E501
        dbc.NavLink("Batch Prediction", href="/app/upload", className="page-link",  # NOQA E501
                    style={"color": "#f5f0ed", "background-color": "#2c65fb"}),
        html.Br(style={"margin-top": "2.5px"}),  # NOQA E501
        # dbc.NavLink("Model Details", href="/app/model_info", className="page-link",  # NOQA E501
        #     style={"color": "#f5f0ed", "background-color": "#2c65fb"}),
        # html.Br(style={"margin-top": "2.5px"}),  # NOQA E501
        dbc.NavLink("Contact Details", href="/app/contact", className="page-link",  # NOQA E501
            style={"color": "#f5f0ed", "background-color": "#2c65fb"})],  # NOQA E501
            vertical=True,
            pills=True,
            ), html.Br(),
    html.Img(src='./assets/common_logo.png',  # NOQA E501
             style={"max-width": "225px", "height": "auto", "margin": "0.27rem", "background-color": ""}),  # NOQA E501
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# app layout

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    html.Div(id='output-data-upload'), ],
    style={"body-bg": "#f1f2f2"}
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    # if pathname == '/app/model_info':
    #     return model_info.layout
    if pathname == '/app/textbox':
        return textbox.layout
    if pathname == '/app/upload':
        return upload.layout
    if pathname == '/app/contact':
        return contact.layout
    else:
        return textbox.layout


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=80, debug=False)  # NOQA E501
