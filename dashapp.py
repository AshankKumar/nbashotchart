import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

court_shapes = []
 
outer_lines_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-250',
    y0='-47.5',
    x1='250',
    y1='422.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(outer_lines_shape)

hoop_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='7.5',
    y0='7.5',
    x1='-7.5',
    y1='-7.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(hoop_shape)

backboard_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-30',
    y0='-7.5',
    x1='30',
    y1='-6.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    ),
    fillcolor='rgba(10, 10, 10, 1)'
)
 
court_shapes.append(backboard_shape)

outer_three_sec_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-80',
    y0='-47.5',
    x1='80',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(outer_three_sec_shape)

inner_three_sec_shape = dict(
    type='rect',
    xref='x',
    yref='y',
    x0='-60',
    y0='-47.5',
    x1='60',
    y1='143.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(inner_three_sec_shape)

left_line_shape = dict(
    type='line',
    xref='x',
    yref='y',
    x0='-220',
    y0='-47.5',
    x1='-220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(left_line_shape)

right_line_shape = dict(
    type='line',
    xref='x',
    yref='y',
    x0='220',
    y0='-47.5',
    x1='220',
    y1='92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)   
 
court_shapes.append(right_line_shape)

three_point_arc_shape = dict(
    type='path',
    xref='x',
    yref='y',
    path='M -220 92.5 C -70 300, 70 300, 220 92.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(three_point_arc_shape)

center_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='482.5',
    x1='-60',
    y1='362.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(center_circle_shape)

res_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='20',
    y0='442.5',
    x1='-20',
    y1='402.5',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(res_circle_shape)

free_throw_circle_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='60',
    y0='200',
    x1='-60',
    y1='80',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1
    )
)
 
court_shapes.append(free_throw_circle_shape)

res_area_shape = dict(
    type='circle',
    xref='x',
    yref='y',
    x0='40',
    y0='40',
    x1='-40',
    y1='-40',
    line=dict(
        color='rgba(10, 10, 10, 1)',
        width=1,
        dash='dot'
    )
)
 
court_shapes.append(res_area_shape)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(
        children="NBA Shotchart",
        style={
            'textAlign': 'center',
        }
    ),
    html.Div(children='Shot data for Brook Lopez in 2018-19', style={
        'textAlign': 'center',
    }),
    dcc.Graph(
        figure={
            'data':[
                {
                    'x':[-100],
                    'y':[100]
                }
            ],
            'layout': go.Layout( #{
                shapes= court_shapes,
                height=800,
                width=1000,
                xaxis= dict(
                    showgrid=False,
                    range=[-300, 300],
                    showticklabels=False,
                    zeroline=False
                ),
                yaxis= dict(
                    showgrid=False,
                    range=[-100, 500],
                    showticklabels=False,
                    zeroline=False
                )
            )
                # 'shapes': court_shapes,
                # 'height': 800,
                # 'width': 1000,
                # xaxis=dict(
                #     showgrid=False,
                #     range=[-300, 300],
                #     showticklabels=False,
                #     zeroline=False
                # ),
                # yaxis=dict(
                #     showgrid=False,
                #     range=[-100, 500],
                #     showticklabels=False,
                #     zeroline=False
                # )
            # }
        }
    )#,
    # html.Div(className='row', children= [
    #     html.Div([
    #         dcc.Input(id='playerName-state', type='text', value='Brook Lopez'),
    #         dcc.Input(id='season-state', type='text', value='2018-2019')
    #         #html.Button(id='submit-button', type='submit', children='Submit'), #changing type='submit' with n_clicks=0 seems to make no difference...
    #     ],
    #     style = dict(
    #         verticalAlign = "middle"
    #         )
    #     )
    # ])
],style = {'margin': 'auto', 'width': "50%"})


# @app.callback(Output('output-state', 'children'),
#               [Input('submit-button', 'n_clicks')],
#               [State('input-1-state', 'value'),
#                State('input-2-state', 'value')])
# def update_output(clicks, input1, input2):
#     return u'''
#         Input 1 is "{}",
#         and Input 2 is "{}"
#     '''.format(input1, input2) #have to take in clicks input but just don't format it xd


if __name__ == '__main__':
    app.run_server(debug=True)