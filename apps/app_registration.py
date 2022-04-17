import json

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk
import plotly
import pandas as pd
import dash_enterprise_auth as auth

import base64
import os
from urllib.parse import quote as urlquote

import sqlalchemy as db
import psycopg2
import sqlalchemy.pool as pool
from sqlalchemy import create_engine, text
from tenacity import retry, wait_exponential, stop_after_attempt

from app import app, postgres_engine

def layout():
    layout = html.Div(
        [
            ddk.Row(
                [
                    ddk.ControlCard(
                        width=100,
                        children=[
                            ddk.CardHeader(
                                title="Please fill out the following information for your VAULT 101 Registration."
                            ),
                            ddk.Row([
                                ddk.ControlItem(
                                    dcc.Dropdown(
                                            id='rank',
                                            options=[
                                                {'label': 'NH-01', 'value': 'NH-01'},
                                                {'label': 'NH-02', 'value': 'NH-02'},
                                                {'label': 'NH-03', 'value': 'NH-03'},
                                                {'label': 'NH-04', 'value': 'NH-04'},
                                                {'label': 'GS-07', 'value': 'GS-07'},
                                                {'label': 'GS-09', 'value': 'GS-09'},
                                                {'label': 'GS-11', 'value': 'GS-11'},
                                                {'label': 'GS-12', 'value': 'GS-12'},
                                                {'label': 'GS-13', 'value': 'GS-13'},
                                                {'label': 'GS-14', 'value': 'GS-14'},
                                                {'label': 'GS-15', 'value': 'GS-15'},
                                                {'label': 'SES', 'value': 'SES'},
                                                {'label': 'Cadet', 'value': 'Cadet'},
                                                {'label': '2d Lt', 'value': '2d Lt'},
                                                {'label': '1st Lt', 'value': '1st Lt'},
                                                {'label': 'Capt', 'value': 'Capt'},
                                                {'label': 'Maj', 'value': 'Maj'},
                                                {'label': 'Lt Col', 'value': 'Lt Col'},
                                                {'label': 'Col', 'value': 'Col'},
                                                {'label': 'Brig Gen', 'value': 'Brig Gen'},
                                                {'label': 'Maj Gen', 'value': 'Maj Gen'},
                                                {'label': 'Lt Gen', 'value': 'Lt Gen'},
                                                {'label': 'Gen', 'value': 'Gen'},
                                                {'label': 'Cadet', 'value': 'Cadet'},
                                                {'label': 'Amn', 'value': 'Amn'},
                                                {'label': 'A1C', 'value': 'A1C'},
                                                {'label': 'SrA', 'value': 'SrA'},
                                                {'label': 'SSgt', 'value': 'SSgt'},
                                                {'label': 'TSgt', 'value': 'TSgt'},
                                                {'label': 'MSgt', 'value': 'MSgt'},
                                                {'label': 'SMSgt', 'value': 'SMSgt'},
                                                {'label': 'CMSgt', 'value': 'CMSgt'},
                                                {'label': 'Contractor', 'value': 'Contractor'},
                                            ],
                                        ),
                                    label="Grade",
                                ),
                                ddk.ControlItem(
                                    dcc.Input(id="first-name", type="text"),
                                    label="First Name",
                                ),
                                ddk.ControlItem(
                                    dcc.Input(
                                        id="last-name", type="text"
                                    ),
                                    label="Last Name",
                                ),
                                ddk.ControlItem(
                                    dcc.Input(
                                        id="email", type="email"
                                    ),
                                    label="E-mail",
                                ),
                                ddk.ControlItem(
                                    dcc.Input(
                                        id="afsc", type="text"
                                    ),
                                    label="AFSC/Series",
                                ),
                            ]),
                            ddk.Row([
                                ddk.ControlItem(
                                    dcc.Input(id="unit", type="text"),
                                    label="Unit",
                                ),
                                ddk.ControlItem(
                                    dcc.Input(
                                        id="base", type="text"
                                    ),
                                    label="Base",
                                ),
                                ddk.ControlItem(
                                    dcc.Dropdown(
                                            id='session',
                                            options=[
                                                {'label': '3-4 May 2022', 'value': 'May 3-4 2022'},                                
                                            ],
                                        ),
                                    label="Desired Session",
                                ),
                            ]),
                            ddk.Row([
                                ddk.ControlItem(
                                    dcc.RadioItems(
                                        id="vaultxp",
                                        options=[
                                            {'label': 'Yes', 'value': '1'},
                                            {'label': 'No', 'value': '0'},
                                        ],
                                    ),
                                    label='Do you have previous experience working with VAULT?'
                                ),
                                ddk.ControlItem(
                                    dcc.RadioItems(
                                        id="codexp",
                                        options=[
                                            {'label': 'Yes', 'value': '1'},
                                            {'label': 'No', 'value': '0'},                                            
                                        ],
                                    ),
                                    label='Do you have previous Coding Experience?'
                                ),                                                               
                            ]),
                            ddk.Row([
                                ddk.ControlItem(
                                    dcc.Checklist(
                                        id="learn-tools",
                                        options=[
                                            {'label': 'VAULT in general', 'value': 'VAULTgen'},
                                            {'label': 'Cloud Environment', 'value': 'Cloud Environment'},                                            
                                            {'label': 'Dash Enterprise', 'value': 'Dash'},
                                            {'label': 'Databricks', 'value': 'Databricks'},                                            
                                            {'label': 'Dataiku', 'value': 'Dataiku'}, 
                                            {'label': 'Git', 'value': 'Git'},
                                            {'label': 'Hue', 'value': 'Hue'},                                            
                                            {'label': 'Jupyter Notebooks', 'value': 'Jupyter Notebooks'},                                            
                                            {'label': 'Plotly', 'value': 'Plotly'},
                                            {'label': 'Python', 'value': 'Python'},
                                            {'label': 'R', 'value': 'R'},
                                            {'label': 'R Shiny', 'value': 'R Shiny'},                                            
                                            {'label': 'Tableau', 'value': 'Tableau'},
                                            {'label': 'Zeppelin', 'value': 'Zeppelin'},                                            
                                            {'label': 'Other (Please mention in comments)', 'value': 'Other'},                                            
                                        ],
                                    ),
                                    label='What tools are you most interested in learning about?'
                                ),
                                ddk.ControlItem(
                                    dcc.Textarea(
                                        id='comments',
                                        value='Please provide any additional comments here.',
                                        style={'width': '100%', 'height': 300},
                                    ),                                    
                                ), 
                            ]),                           
                            ddk.Modal(
                                children=[
                                    html.Button("Submit your Registration", id="button-main-one", n_clicks=0)
                                ],
                                target_id='successful-submit',
                                hide_target=True,
                            ),
                            dcc.Markdown(id='successful-submit', children = [
                                    '''
                                    Thank you for registering for VAULT 101!

                                    Your registration was successfully received!

                                    Once confirmed, you will receive a welcome email prior to the course start date.
                                    '''
                                    ]
                            ),
                        ],
                    ),
                ]
            )
        ]
    )
    return layout


@app.callback(
    [Output("first-name", "value"), Output("last-name", "value"), Output("rank", "value"), Output("afsc", "value"), Output("unit", "value"), Output("base", "value"), Output("session", "value"), Output("email", "value"), Output("vaultxp", "value"), Output("codexp", "value"), Output("learn-tools", "value"), Output("comments", "value")],
    [Input("button-main-one", "n_clicks")],
    [State("first-name", "value"), State("last-name", "value"), State("rank", "value"), State("afsc", "value"), State("unit", "value"), State("base", "value"), State("session", "value"), State("email", "value"), State("vaultxp", "value"), State("codexp", "value"), State("learn-tools", "value"), State("comments", "value")],
)
def update_registrations(n_clicks, firstname, lastname, rank, afsc, unit, base, session, email, vaultxp, codexp, learntools, comments):
    username = auth.get_username()
    if n_clicks >= 1:
        my_dict = {"first_name": [firstname], "last_name": [lastname], "grade": [rank], "afsc": [afsc], "unit": [unit], "base":[base], "desired_session":[session], "email":[email], "vaultxp":[vaultxp], "codexp":[codexp], "learn_tools":[learntools], "comments":[comments]}

        current_registration = pd.read_sql('SELECT * FROM registration', postgres_engine)
        #current_registration = pd.read_csv('presentation.csv')
        new = pd.DataFrame.from_dict(my_dict)
        print(new)
        new_registration = current_registration.append(new)
        #new_registration.set_index(keys='email')
        # In the following command, we are saving the updated new data to the registration table using pandas
        # and the SQLAlchemy engine we created above. When if_exists='append' we add the rows to our table
        # and when if_exists='replace', a new table overwrites the old one.
        new_registration.to_sql(name = "registration", con = postgres_engine, if_exists="replace", index=False)

        #return is a blank for each value to clear the input for the next person.  
        return "", "", "", "", "", "","", "", "", "", "", ""
    else:
        raise dash.exceptions.PreventUpdate
