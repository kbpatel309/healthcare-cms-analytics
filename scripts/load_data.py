# pip install pandas psycopg2 sqlalchemy - install dependencies

import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv('data/Hospital_General_Information.csv')

# Create database connection
