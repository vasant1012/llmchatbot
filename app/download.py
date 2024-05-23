# import dash
from datetime import datetime
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
from dash import dcc
import pandas as pd
from dash import html
from main import app
import pathlib
import warnings
warnings.filterwarnings('ignore')

PATH = pathlib.Path(__file__).parent

download_filename = f'Batch_Prediction_Results_{str(datetime.now().replace(microsecond=0))}.csv'  # NOQA E501
download_filename = download_filename.replace(' ', '_').replace(':', '_')  # NOQA E501

layout = html.Div([dbc.Button("Download", id="btn_csv", external_link=True, style={"background-color": "#2c65fb", "height": "40px"}),  # NOQA E501
                 dcc.Download(id="download-dataframe-csv")], style={"padding": "1rem 1rem"})  # NOQA E501


@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    df = pd.read_pickle("./app/df.pkl")
    return dcc.send_data_frame(df.to_csv, download_filename, index=False)
