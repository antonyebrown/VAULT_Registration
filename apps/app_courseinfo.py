import json
import random

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

from app import app

context = """
The documents below contain course information and prerequisites:

[Getting Started with VAULT](https://plotly-enterprise-afac.afdatalab.af.mil/Workspaces/edit/vault-101/files/download/?id=a627c8e2-138d-46a4-b35c-80a7b0e35ad4)

[VAULT 101 Intro and Prerequisites](https://plotly-enterprise-afac.afdatalab.af.mil/Workspaces/edit/vault-101/files/download/?id=8611657d-453c-4a3c-9112-f5de3651afe3)

[VAULT 101 Current Course Schedule](https://plotly-enterprise-afac.afdatalab.af.mil/Workspaces/edit/vault-101/files/download/?id=2ec6549f-9ab4-4fd6-a31e-a167b214b3dc)

Please take the time before the course to look over the intro and pre-req instructions and ensure that you have access to the following in VAULT:
	
* Access to Databricks and either the AFAC, AFOTEC, or AFDV cluster
	
* Access to Tableau in VAULT or a free Tableau public account (https://public.tableau.com)

 
If you run into any problems with these instructions, please either put in a help desk ticket on VAULT or contact Capt Antony Brown at antony.brown@us.af.mil or Lt Alec Sekelsky at alec.sekelsky.1@us.af.mil for further assistance.

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
                            dcc.Markdown(context),
                        ],
                    ),
                ],
            ),
        ]
    )
    return layout



