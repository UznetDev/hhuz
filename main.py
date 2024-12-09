import streamlit as st
from loader import data
import plotly.express as px



st.set_page_config(page_title="HH Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")


col1, col2 = st.columns(2)

category_counts = data['expreince'].value_counts().reset_index()
category_counts.columns = ['Expreince', 'Count']


fig = px.pie(category_counts, values='Count', names='Expreince', 
             title='Expreince Distribution', hole=0.1)

fig.update_traces(pull=[0.02, 0.05, 0.01, 0.105],
                 textinfo='percent+label',
                 marker=dict(line=dict(color='white', width=2)))

fig.update_layout(
    font=dict(size=16, color='#F39C12'),
    showlegend=True, 
    title_font_size=20,
    title_x=0.5,
    margin=dict(t=30, b=0, l=0, r=0),
                )

with col1:
    st.plotly_chart(fig)



fig_hist = px.histogram(data, x='category', color='starter',
                        title='Category Distribution with Starter Hue',
                        labels={'starter': 'Starter'},
                        barmode='group')


fig_hist.update_layout(
    xaxis_title='Category',
    yaxis_title='Count',
    xaxis={'categoryorder': 'total descending'}
)

with col2:
    st.plotly_chart(fig_hist)



title_counts = data[data['category'] == 'Other']['title'].value_counts().reset_index().head(20)
title_counts.columns = ['Title', 'Count']


fig_bar = px.bar(title_counts,
                x='Title',
                y='Count',
                color='Count',
                title='Title Distribution with Colors Based on Count in Other Category.',
                color_continuous_scale='Viridis')


fig_bar.update_layout(
    xaxis_title='Title',
    yaxis_title='Count',
    xaxis={'categoryorder': 'total descending'},
    showlegend=False
)

st.write(fig_bar)