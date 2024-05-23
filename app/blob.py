from main import app
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
from dash import html
import pathlib
import warnings
warnings.filterwarnings('ignore')

PATH = pathlib.Path(__file__).parent

layout = html.Div([dbc.Button("Upload to Blob", id="blob-button", n_clicks=0,
                                style={"background-color": "#292929", "height": "40px"}),  # NOQA E501
                                html.Div(id="upload-blob", style={"verticalAlign": "middle", "padding": "1rem 1rem"}), ])  # NOQA E501


@app.callback(Output('upload-blob', 'children'),
              Input('blob-button', 'n_clicks'),
              prevent_initial_call=True,
              )
def blob_upload(n_clicks):
    if n_clicks > 0:
        import os
        import pandas as pd
        from datetime import datetime
        from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient  # NOQA E501
        df = pd.read_pickle("./app/df.pkl")
        download_filename = f'Batch_Prediction_Results_{str(datetime.now().replace(microsecond=0))}.csv'  # NOQA E501
        download_filename = download_filename.replace(' ', '_').replace(':', '_')  # NOQA E501
        df.to_csv(download_filename, index=False)
        connect_str = os.environ.get("BLOB_CONNECTION_STR")
        container_name = os.environ.get("RESULTS_DATA_CONTAINER")
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)  # NOQA E501
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=download_filename)  # NOQA E501
        with open(download_filename, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print("File uploaded: " + download_filename)
        os.remove(download_filename)
        message = f"Uploaded successfully to storage container - {container_name}/{download_filename}"  # NOQA E501
        return html.Div([html.H6(message)],  # NOQA E501
                          style={"position": "absolute", "top": "250px", "margin-left": "150px"})  # NOQA E501
    else:
        pass
