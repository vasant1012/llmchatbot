import base64
from datetime import datetime
import io
import os
import pickle
from pygpt import gptbot
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import numpy as np
from main import app
from app import download, blob
import pathlib
import warnings

warnings.filterwarnings('ignore')

PATH = pathlib.Path(__file__).parent

layout = html.Div([
    html.H2("Batch Prediction",
            className="display-5",
            style={'textAlign': 'top-center'}),  # NOQA E501
    dcc.Upload(
        id='upload-data',
        children=html.Div(
            'Click to select file Or Drag and Drop'),  # NOQA E501
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '55px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'position': 'relative',
            'margin': '10px',
            "background-color": "#2c65fb",
            "color": "white",
            'font-weight': 'bold'
        },
        multiple=True),
    html.Div(id='output-data-upload'),
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    file = open('./app/docsearch.pkl', 'rb')
    docsearch = pickle.load(file)
    file.close()
    global df
    if '.csv' in filename:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        if 'Question' in df.columns:
            text = list(np.array(df['Question'].values).flat)
            answers = []
            for i in text:
                answer = gptbot.chatbot(i, docsearch)
                answers.append(answer)
            answer = "This is the reply from gptbot."  # NOQA E501
            df0 = pd.DataFrame(
                data=answers,
                columns=["Answer by GPT"]) 
            df = pd.concat([df, df0], axis=1)
            df.to_pickle("./app/df.pkl")
            file_info = f'Batch Filename - {filename}. No. of records - {df.shape[0]}. Prediction Date & Time -     {datetime.now().replace(microsecond=0)}'  # NOQA E501
            download_filename = f'Batch_Prediction_Results_{str(datetime.now().replace(microsecond=0))}.csv'  # NOQA E501
            download_filename = download_filename.replace(' ', '_').replace(
                ':', '_')
            return html.Div(
                [
                    html.P(file_info),
                    html.Hr(style={"height": "2px", "color": "#00488E"}),
                    html.Div([download.layout],
                             style={"display": "inline-block"}),  # NOQA E501
                    # html.Span([blob.layout],
                    #           style={
                    #               "display": "inline-block",
                    #               "column-span": "all"
                    #           }),  # NOQA E501
                    html.Br(),
                    dbc.Table.from_dataframe(
                        df,
                        bordered=True,
                        style={  # NOQA E501
                            'textAlign': 'center',
                            "background-color": "#f1f2f2"
                        }),  # NOQA E501
                    html.Hr(style={"height": "2px", "color": "#00488E"}),
                ],
                style={"padding": "1rem 1rem"})
        else:
            return html.Div([
                html.Br(),
                html.Hr(style={"height": "1px", "color": "#00488E"}),
                html.Br(),
                html.Br(),
                html.H3(
                    "Please provide file which contain 'Question' in columns.",  # NOQA E501
                    style={
                        'textAlign': 'center',
                        "background-color": "#f1f2f2"
                    }),  # NOQA E501
                html.Br(),
                html.Hr(style={"height": "1px", "color": "#00488E"})
            ])

    elif '.xlsx' in filename or '.xls' in filename:
        df = pd.read_excel(io.BytesIO(decoded))
        if 'Question' in df.columns :
            text = list(np.array(df['Question'].values).flat)
            answers = []
            for i in text:
                answer = gptbot.chatbot(i, docsearch)
                answers.append(answer)
            answer = "This is the reply from gptbot."  # NOQA E501
            df0 = pd.DataFrame(
                data=answers,
                columns=["Answer by GPT"]) 
            df = pd.concat([df, df0], axis=1)
            file_info = f'Batch Filename - {filename}. No. of records - {df.shape[0]}. Prediction Date & Time -     {datetime.now().replace(microsecond=0)}'  # NOQA E501
            download_filename = f'Batch_Prediction_Results_{str(datetime.now().replace(microsecond=0))}.csv'  # NOQA E501
            download_filename = download_filename.replace(' ', '_').replace(
                ':', '_')  # NOQA E501
            return html.Div(
                [
                    html.P(file_info),
                    html.Hr(style={"height": "1px", "color": "#00488E"}),
                    html.Div([download.layout],
                             style={"display": "inline-block"}),  # NOQA E501
                    # html.Span([blob.layout],
                    #           style={
                    #               "display": "inline-block",
                    #               "column-span": "all"
                    #           }),  # NOQA E501
                    html.Br(),
                    dbc.Table.from_dataframe(
                        df,
                        bordered=True,
                        style={  # NOQA E501
                            'textAlign': 'center',
                            "background-color": "#f1f2f2"
                        }),  # NOQA E501
                    html.Hr(style={"height": "2px", "color": "#00488E"}),
                ],
                style={"padding": "1rem 1rem"})
        else:
            return html.Div([
                html.Br(),
                html.Hr(style={"height": "1px", "color": "#00488E"}),
                html.Br(),
                html.Br(),
                html.H3(
                    "Please provide file which contain 'Title' and 'Scenario' in columns.",  # NOQA E501
                    style={
                        'textAlign': 'center',
                        "background-color": "#f1f2f2"
                    }),  # NOQA E501
                html.Br(),
                html.Hr(style={"height": "1px", "color": "#00488E"})
            ])
    else:
        return html.Div([
            html.Br(),
            html.Hr(style={"height": "1px", "color": "#00488E"}),
            html.Br(),
            html.Br(),
            html.H3(
                'Please provide file in either ".csv" or ".xls" format.',  # NOQA E501
                style={
                    'textAlign': 'center',
                    "background-color": "#f1f2f2"
                }),  # NOQA E501
            html.Br(),
            html.Hr(style={"height": "1px", "color": "#00488E"})
        ])


@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'), State('upload-data',
                                                      'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children
