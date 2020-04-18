import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data.csv', index_col=0)
df = df.replace(np.nan, 0)
df = df.dropna()

weight = [go.Scatter(
    x=df.index,
    y=df[col],
    mode='lines+markers',
    name=col) for col in df.columns]

# TEST
# workout_volume = [go.Scatter(
#     x=df.index,
#     y=df[col],
#     mode='lines+markers',
#     name=col) for col in df.columns]

layout = go.Layout(title='WEIGHT STATISTICS',
                   xaxis=dict(title='TIME'),
                   yaxis=dict(title='Weight properties'),
                   hovermode='closest')

data = [*weight]

fig = go.Figure(data=data[0:], layout=layout)

pyo.plot(fig, filename='weight_stats.html')
