import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Electricity Price Tracker")
st.title("Real-time Electricity Prices")

def load_data():
    data = []
    try:
        with open("output.json", "r") as f:
            for line in f:
                data.append(json.loads(line))
    except FileNotFoundError:
        return pd.DataFrame()
    
    df = pd.DataFrame(data)
    if not df.empty:
        df['startDate'] = pd.to_datetime(df['startDate'])
        df = df.sort_values('startDate')
    return df

# Streamlit UI
df = load_data()

if not df.empty:
    st.subheader("Price Over Time")
    st.line_chart(df.set_index('startDate')['price'])
    
    st.subheader("Raw Data")
    st.write(df)
else:
    st.write("No data found in output.json yet.")

if st.button('Refresh Data'):
    st.rerun()