import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')

# Getting max temp for each month
new_df = df.groupby(['month']).max(['actual_max_temp']).reset_index()

# Preparing data
data = [go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], mode='lines', name='Temperature')]

# Preparing layout
layout = go.Layout(title='Actual Max Temperatures by Month', xaxis_title="Month",
                   yaxis_title="Max Temperature")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechart.html')
