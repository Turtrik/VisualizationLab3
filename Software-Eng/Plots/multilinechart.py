import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Getting max temp for each month
new_df = df.groupby(['month']).max(['actual_max_temp']).reset_index()
trace1 = go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Max Temperature')

# Getting min temp for each month
new_df = df.groupby(['month']).min(['actual_min_temp']).reset_index()
trace2 = go.Scatter(x=new_df['month'], y=new_df['actual_min_temp'], mode='lines', name='Min Temperature')

# Getting mean temp for each month
new_df = df.groupby(['month']).mean(['actual_mean_temp']).reset_index()
trace3 = go.Scatter(x=new_df['month'], y=new_df['actual_mean_temp'], mode='lines', name='Avg Temperature')

# Preparing data
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(title='Actual Max/Min/Mean Temperatures by Month', xaxis_title="Month",
                   yaxis_title="Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilinechart.html')
