import sqlite3
import pandas as pd
from config import settings

def extract_from_sqlite():
    conn = sqlite3.connect(settings.SQLITE_DB_PATH)
    df = pd.read_sql_query("SELECT * FROM customers", conn)
    conn.close()
    return df.to_dict(orient='records')
