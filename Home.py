import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title('Kanvas.AI Art Index')

st.header('Allee Galerii Auctions - Map of Art Market')

st.subheader(
  'Who are the best selling artists? Total art auction sales by overbidding percentage'
)

df = pd.read_csv('allee_clean.csv')
df['overbid_%'] = (df['end_price'] -
                   df['start_price']) / df['start_price'] * 100
df['art_work_age'] = df['date'] - df['year']
df2 = df.groupby(['author', 'tech', 'category']).agg({
  'end_price': ['sum'],
  'overbid_%': ['mean']
})
df2.columns = ['total_sales', 'overbid_%']
df2 = df2.reset_index()
df2['overbid_%'] = df2['overbid_%'] * 100

fig = px.treemap(df2,
                 path=['category', 'tech', 'author'],
                 values='total_sales',
                 color='overbid_%',
                 hover_data=['author'],
                 color_continuous_scale='RdBu',
                 color_continuous_midpoint=np.average(
                   df2['overbid_%'], weights=df2['total_sales']))

st.plotly_chart(fig, use_container_width=True)

st.subheader(
  'Is older art more expensive? The relationship between the age of the art work and price'
)

fig = px.scatter(df,
                 x="art_work_age",
                 y="end_price",
                 color="category",
                 size='decade',
                 hover_data=['author'])

st.plotly_chart(fig, use_container_width=True)

st.subheader(
  'Are larger art works more expensive? The relationship between the dimensions of an art work and its price'
)

fig = px.scatter(df,
                 x="dimension",
                 y="end_price",
                 color="category",
                 size='dimension',
                 hover_data=['author'])

st.plotly_chart(fig, use_container_width=True)

st.text('Author: Julian Kaljuvee')
st.text('Source: Allee Galerii auctions (2020-2022)')
