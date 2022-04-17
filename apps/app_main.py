import json
import random

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_design_kit as ddk

from app import app

context = """
**Welcome to the VAULT 101 (Intro to Air Force Data Lab) registration page!** Please use the links on the top of the page to submit and view your registration status. 
         
This 2 day virtual course serves an "all-around" introduction and guide to using many of VAULT's main features: S3 Cloud Storage via Hue, Databricks, Plotly, R Shiny, and Tableau. You'll also learn how to quickly manipulate and analyze your data using Python and R.  There are fantastic learning resources available for each one of these topics specifically, but this course is designed to show you end-to-end use cases that will get you comfortable using VAULT in just 2 days. By the end of this course, you will be able to take raw data in various formats, analyze it, and turn it into a useful visualization-- all within the VAULT environment!

If you can’t attend the full 2 days, that’s okay.  You’re welcome to still sign up and attend whatever portions you’re able to, please just be sure to briefly describe your planned level of participation when you sign up (for our awareness & planning).

VAULT 101 prerequisites, Getting Started with VAULT, & current course schedule are all located within the "Course Info" section to help you make an informed decision. Please don't let a lack of coding knowledge stop you from signing up- we will work in teams to spread our abilities so that no one gets left behind.  **Class size is limited to 21 students per session, so if we can't get you in to your preferred session, please stay tuned for future offerings.**  Recordings of the class will be made available on the AFAC Teams page for those unable to attend.
 
Thank you!

**Upcoming course dates:** 
* 3-4 May 2022

For questions or assistance, please contact Capt Antony Brown at antony.brown@us.af.mil or Lt Alec Sekelsky at alec.sekelsky.1@us.af.mil.


*This registration site was built with Plotly Enterprise by Capt Antony Brown, adapted from work by Maj Brian Fagan.* 
            """


def layout():
    layout = html.Div(
        [
            ddk.Row(
                [
                    ddk.Card(
                        width=100,
                        children=[
                            ddk.CardHeader(title="VAULT 101 (Intro to Air Force Data Lab) Course Registration"),
                            dcc.Markdown(context),
                        ],
                    ),
                ],
            ),
        ]
    )
    return layout



