#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# In[14]:


df = pd.read_csv("cases.csv")


# In[15]:


st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")


# In[16]:


select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox("Hide", True, key='count'):
    if select == 'Pie chart':st.title("Selected top 5 cities")
fig = px.pie(df, values=df['Confirmed'][:5], names=df['State'][:5], title='Total Confirmed Cases')
st.plotly_chart(fig)

if select=='Bar plot':st.title("Selected Top 5 Cities")
fig = go.Figure(data=[go.Bar(name='Confirmed', x=df['State'][:5], y=df['Confirmed'][:5]),go.Bar(name='Recovered', x=df['State'][:5], y=df['Recovered'][:5]),go.Bar(name='Deceased', x=df['State'][:5], y=df['Deceased'][:5])])
st.plotly_chart(fig)

