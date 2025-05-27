# pip install pandas psycopg2 sqlalchemy - install dependencies

import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv('../data/Hospital_General_Information.csv')

# Create database connection to PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')

# Load data into PostgreSQL
# Make sure there are 38 columns in the table
try:
    df.to_sql('hospital_info', engine, if_exists='replace', index=False)
    print("✅ Data loaded successfully into 'hospital_info' table.")
except Exception as e:
    print("❌ Failed to load data:", e)


