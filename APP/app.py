import streamlit as st
import pandas as pd
import snowflake.connector

SNOWFLAKE_USER = "YOUR_USERNAME"
SNOWFLAKE_PASSWORD = "YOUR_PASSWORD"
SNOWFLAKE_ACCOUNT = "YOUR_ACCOUNT"
SNOWFLAKE_WAREHOUSE = "YOUR_WAREHOUSE"
SNOWFLAKE_DATABASE = "TSI_CLASSWORK_9"
SNOWFLAKE_SCHEMA = "MY_SCHEMA"


@st.cache_data(ttl=300)
def get_data():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )

    query = "SELECT * FROM EU_ADDRESSES LIMIT 1000"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


st.title("EU Addresses Dashboard")

st.markdown(
    """
    This app displays addresses from European Union countries from Snowflake.
    """
)

df = get_data()

st.write(f"Showing {len(df)} rows from EU_ADDRESSES table")
st.dataframe(df)
