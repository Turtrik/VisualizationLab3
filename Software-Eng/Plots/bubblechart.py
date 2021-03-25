# Draw a bubble chart to represent the average min and max temperature of each month in weather statistics

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


df = pd.read_csv('../Datasets/Weather2014-15.csv')

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
df['month'] = pd.Categorical(df['month'], categories=months, ordered=True)

new_df = df.groupby(['month']).agg(
    {'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()

data = [
    go.Scatter(x=new_df['average_min_temp'],
               y=new_df['average_max_temp'],
               text=new_df['month'],
               mode='markers',
               marker=dict(size=((new_df['average_min_temp'] + new_df['average_max_temp']) / 2),
                           color=((new_df['average_min_temp'] + new_df['average_max_temp']) / 2),
                           showscale=True)
               )
]

# Preparing layout
layout = go.Layout(title='Avg min/max of each month', xaxis_title="Average min temp",
                   yaxis_title="Average max temp", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechart.html')

print(df)
print(new_df)

