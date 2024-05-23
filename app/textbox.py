# import dash
from dash.dependencies import Input, Output, State
from dash import html
from pygpt import gptbot
# from dash import dcc
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import pickle
from main import app
import warnings
warnings.filterwarnings('ignore')


PATH = pathlib.Path(__file__).parent

layout = html.Div([html.H2("User Input Question", className="display-5", style={'textAlign': 'center'}),  # NOQA E501
                  html.Div([html.Br(),
                            dbc.Textarea(id='textarea-state-example-query', placeholder="Please type in your Question related to RBI trained PDF Files",  # NOQA E501
                                         value=''.format(),
                                         style={'width': '100%', 'height': 60}),  # NOQA E501
                            html.Br(),
                            dbc.Button('Submit', id='textarea-state-example-button', n_clicks=0,  # NOQA E501
                                       style={"background-color": "#2c65fb", "height": "40px"})]),  # NOQA E501
                   html.Br(),
                   html.Div(id='textarea-state-example-output', style={'whiteSpace': 'pre-line'})],  # NOQA E501
                  )


@app.callback(
    Output('textarea-state-example-output', 'children'),
    [Input('textarea-state-example-button', 'n_clicks')],
    [State('textarea-state-example-query', 'value')],
)
def update_output(n_clicks, query):
    if n_clicks > 0 and not query:
        print(n_clicks)
        return "No text entered in text area. Please enter the text in above box."  # NOQA E501
    elif n_clicks > 0 and query:
        file = open('./app/docsearch.pkl', 'rb')
        docsearch = pickle.load(file)
        file.close()
        query = str(query)
        df = pd.DataFrame({"Query": [query]})
        answer = gptbot.chatbot(query, docsearch)
        # answer = "This is the reply from gptbot."
        df_out = pd.DataFrame({"Answer": [answer]})  # NOQA E501
        df = pd.concat([df, df_out], axis=1)
        table = dbc.Table.from_dataframe(df, bordered=True,
                                         style={'textAlign': 'center', "background-color": "#f1f2f2"})  # NOQA E501
        return table
