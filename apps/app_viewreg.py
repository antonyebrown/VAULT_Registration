import json

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk
import plotly
import dash_table
import pandas as pd

import base64
import os
from urllib.parse import quote as urlquote

import sqlalchemy as db
import psycopg2
import sqlalchemy.pool as pool
from sqlalchemy import create_engine, text
from tenacity import retry, wait_exponential, stop_after_attempt

from app import app, postgres_engine

human_readable = ["Grade", "First Name", "Last Name", "Unit", "Base", "Class Date"]

def get_dataframe():
    # In this function, we retrieve the data from postgres using pandas's read_sql method.
    updated_df = pd.read_sql(
        'SELECT "grade", "first_name", "last_name", "unit", "base", "desired_session" FROM registration', postgres_engine
    )
    return updated_df


def layout():
    layout = html.Div(
        [
            html.Div(id='dummy'),
            ddk.Card(
                width=100,
                children=[
                    ddk.CardHeader(title="Successful registrations.  We look forward to seeing you during the course."),
                    dash_table.DataTable(
                        id="SQL-registrations",
                    ),
                ],
            ),
        ]
    )
    return layout


#this uses a dummy input becuase we are using the postgres data to update.
@app.callback(
    Output('SQL-registrations','data'),
    Output('SQL-registrations','columns'),
    Input('dummy','children'),
)
def updatedata(data):
    df = get_dataframe()
    columns=[{"name": n, "id": i} for i, n in zip(df.columns, human_readable)]
    data = df.to_dict("records")
    return data, columns