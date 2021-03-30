import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/CoronavirusTotal.csv')
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df3 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df3.sort_values(by=['Total'], ascending=[False]).head(20)
data_barchart = [go.Bar(x=barchart_df['NOC'], y=barchart_df['Total'])]

# Stack bar chart data
stackbarchart_df = df3.sort_values(by=['Total'], ascending=[False]).head(20)

trace1_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
trace3_stackbarchart = go.Bar(x=stackbarchart_df['NOC'], y=stackbarchart_df['Gold'], name='Gold', marker={'color': '#FFD700'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart, trace3_stackbarchart]

# Line Chart
line_df = df4.groupby(['month'])['actual_max_temp'].max().reset_index()
data_linechart = [go.Scatter(x=line_df['month'], y=line_df['actual_max_temp'], mode='lines', name='Temperature')]

# Multi Line Chart
multiline_df = df4.groupby(['month'])['actual_max_temp'].max().reset_index()
trace1_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_max_temp'], mode='lines', name='Max Temperature')
multiline_df = df4.groupby(['month'])['actual_min_temp'].max().reset_index()
trace2_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_min_temp'], mode='lines', name='Min Temperature')
multiline_df = df4.groupby(['month'])['actual_mean_temp'].max().reset_index()
trace3_multiline = go.Scatter(x=multiline_df['month'], y=multiline_df['actual_mean_temp'], mode='lines', name='Avg Temperature')
data_multiline = [trace1_multiline, trace2_multiline, trace3_multiline]

# Bubble chart
bubble_df = df4.groupby(['month']).agg(
    {'average_min_temp': 'mean', 'average_max_temp': 'mean'}).reset_index()
data_bubblechart = [
    go.Scatter(x=bubble_df['average_min_temp'],
               y=bubble_df['average_max_temp'],
               text=bubble_df['month'],
               mode='markers',
               marker=dict(size=((bubble_df['average_min_temp'] + bubble_df['average_max_temp']) / 2),
                           color=((bubble_df['average_min_temp'] + bubble_df['average_max_temp']) / 2),
                           showscale=True)
               )
]

# Heatmap
data_heatmap = [go.Heatmap(x=df4['day'],
                   y=df4['month'],
                   z=df4['record_max_temp'].values.tolist(),
                   colorscale='Jet')]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represents the total medals of Olympic 2016 of 20 first top countries.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Total Medals in Countries in 2016 Olympics',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Total number of medals'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stacked bar chart represents the Gold, Silver, Bronze medals of Olympic 2016 of 20 first top countries.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Total Medals of Countries in 2016 Olympics',
                                      xaxis={'title': 'Country'}, yaxis={'title': 'Total number of medals'},
                                      barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represents the actual max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='Actual Max Temperatures By Month',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Max Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represents the actual max, min and mean temperature of each month in weather statistics'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(
                      title='Actual Max/Min/Mean Temperatures by Month',
                      xaxis={'title': 'Month'}, yaxis={'title': 'Temperature'})
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
    html.Div(
        'This bubble chart represents the average min and max temperature of each month in weather statistics.'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='Average min/max of each month',
                                      xaxis={'title': 'Average min temp'}, yaxis={'title': 'Average max temp'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represents the recorded max temperature on day of week and month of year.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Recorded Max Temperature',
                                      xaxis={'title': 'Day of Week'}, yaxis={'title': 'Month of Year'})
              }
              )
])


@app.callback(Output('graph1', 'figure'),
              [Input('select-continent', 'value')])
def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()