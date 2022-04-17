import datetime
import pandas as pd
from app import app, postgres_engine

timenow = datetime.datetime.now()

registrations = pd.read_sql(
       'SELECT * FROM registration', postgres_engine
    )

registrations.to_csv(f'archives/registrationbackup_{timenow}.csv', index=True)
