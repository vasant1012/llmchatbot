import dash_bootstrap_components as dbc
from dash import html
import pathlib
import json
import warnings

warnings.filterwarnings('ignore')

PATH = pathlib.Path(__file__).parent

with open('contact_info.json') as f:
    contact = json.load(f)

layout = html.Div([
    html.H2("Contact Us", className="display-5",
            style={'textAlign': 'center'}),
    html.Br(),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5("Contact Information")),
            dbc.CardBody([
                html.P(["Name : ", contact.get("Name")]),
                html.P(["Address : ", contact.get("Address")]),
                html.P(["Office No. : ", contact.get("Office No.")]),
                html.P(["Mobile No. : ", contact.get("Mobile")]),
                html.P(["Email : ", contact.get("Email")]),
            ])
        ],
                         style={'textAlign': 'center'}),
                width=6),
        dbc.Col(dbc.Card([
            dbc.CardHeader(html.H5("Documentation")),
            dbc.CardBody(
                html.P([
                    "Visit - ",
                    dbc.CardLink(
                        "RBI Documentation",
                        href="https://ind01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.rbi.org.in%2FScripts%2FNotificationUser.aspx%3FId%3D12181%26Mode%3D0&data=05%7C01%7Csarankjoseph%40federalbank.co.in%7C8fa2e5dbf8f849eb88f808db1a5f2cad%7C2d5718b7ec0049d29d18feca299cda73%7C0%7C0%7C638132768288976817%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=sR%2BauIDywdHw2gwZ%2FzPChjZ5xNPO64GMrXll%2FC5RKF4%3D&reserved=0",  # NOQA E501
                        style={
                            "color": "blue",
                            "textAlign": "right"
                        })
                ]))
        ],
                         style={'textAlign': 'center'}),
                width={
                    "size": 6,
                    "offset": 0.5
                }),
    ]),
    html.Br(),
],
                  style={"margin": "1.5rem"})
