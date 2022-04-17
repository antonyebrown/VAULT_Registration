import dash
import dash_design_kit as ddk
import os
from sqlalchemy import create_engine, text
from tenacity import retry, wait_exponential, stop_after_attempt
import pandas as pd

app = dash.Dash(__name__)
server = app.server

app.config.suppress_callback_exceptions = True


connection_string = "postgres+psycopg2" + os.environ.get(
    "DATABASE_URL", "postgres://postgres:docker@127.0.0.1:5432"
).lstrip("postgres")

# Creates a SQLAlchemy engine object. This object contains information about our target database
postgres_engine = create_engine(connection_string)


# We use `exponential backoff` to poll the database for a status and make sure
# that it is available for a connection, by sending a basic query at an incremental delay.
# The number of retry attempts as well as the multiplier and time between attempts can be modified if the need arises.
@retry(wait=wait_exponential(multiplier=2, min=1, max=10), stop=stop_after_attempt(5))
def try_connection():
    try:
        with postgres_engine.connect() as connection:
            stmt = text("SELECT 1")
            connection.execute(stmt)
        print("Connection to database successful.")

    except Exception as e:
        print("Connection to database failed, retrying. If connecting to the Plotly-hosted sample database, "
              "then this database instance can take a few minutes to wake from its sleep-state.")
        raise Exception

try_connection()

#Reset the postgres database (or initialize if this is the first time running the app)
#df = pd.read_csv('registration.csv', header=0, index_col=0)
#df.to_sql("registration", postgres_engine, if_exists="replace", index=True)

#df = pd.read_csv('presentation.csv', header=0, index_col=0)
#df.to_sql("presentation", postgres_engine, if_exists="replace", index=True)
