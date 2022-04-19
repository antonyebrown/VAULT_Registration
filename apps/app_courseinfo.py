import json
import random

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

from app import app

context1 = """
The documents below contain course information and prerequisites:

            """

context2 = """
Please take the time before the course to look over the intro and pre-req instructions and ensure that you have access to the following in VAULT:
	
* Access to Databricks and either the AFAC, AFOTEC, or AFDV cluster
	
* Access to Tableau in VAULT or a free Tableau public account (https://public.tableau.com)

 
If you run into any problems with these instructions, please either put in a help desk ticket on VAULT or contact Capt Antony Brown at antony.brown@us.af.mil or Lt Alec Sekelsky at alec.sekelsky.1@us.af.mil for further assistance.

            """

context3 = """
  
            """

def layout():
    layout = html.Div(
        [
            ddk.Row(
                [
                    ddk.Card(
                        width=100,
                        children=[
                            ddk.CardHeader(title="VAULT 101 Course Information"),
                            dcc.Markdown(context1),
                            dcc.Link("Getting Started With Vault", href=("/workspace/documents/Getting Started with Vault.pptx")),
                            dcc.Markdown(context3),
                            dcc.Link("VAULT 101 Intro and Prerequisites", href=("/workspace/documents/VAULT 101 Course--Intro & Prereq's_Feb 2022.docx")),
                            dcc.Markdown(context3),
                            dcc.Link("VAULT 101 Current Course Schedule", href=("/workspace/documents/VAULT 101 Schedule.xlsx")),
                            dcc.Markdown(context2),
                        ],
                    ),
                ],
            ),
        ]
    )
    return layout


@app.callback(
    Output("download-image", "data"),
    Input("btn_image", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_file(
        "./assets/Getting Started with Vault.pptx"
    )

