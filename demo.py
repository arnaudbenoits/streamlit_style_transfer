import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import urllib
import io

st.title('Data Dej - Streamlit Demo')

st.subheader('Load your csv...')
uploaded_file = st.file_uploader('Choose a file')
@st.cache
def load_data(uploaded_file):
    if uploaded_file is not None:
        string_data = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = f'Loaded file: {string_data}'
        data = pd.read_csv(uploaded_file, sep=';') 
        return string_data, data
    else:
        string_data = 'No file found, demo csv loaded'
        data = pd.read_csv('final_all_types.csv') 
        return string_data, data
        

string_data, data = load_data(uploaded_file)
st.write(string_data)

st.subheader('Explore your data')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

@st.cache
def explore_df(df):
    profile = ProfileReport(df, title = 'DataFrame exploration')
    profile.to_file("report.html")

    with open("report.html", "r", encoding='utf-8') as f:
        text = f.read()
    return text

text = explore_df(data)
st.components.v1.html(text, scrolling=True, height=500)

# st.write(df)

# st.text('Et voilà')