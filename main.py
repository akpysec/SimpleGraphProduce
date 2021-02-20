import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data.csv', index_col=0)
df = df.replace(np.nan, 0)
df = df.dropna()

columns = [go.Scatter(
    x=df.index,
    y=df[col],
    mode='lines+markers',
    name=col) for col in df.columns]

layout = go.Layout(title='TITLE',
                   xaxis=dict(title='TIME'),
                   yaxis=dict(title='AMOUNT'),
                   hovermode='closest')

data = [*columns]

fig = go.Figure(data=data[0:], layout=layout)

pyo.plot(fig, filename='Graph.html')
