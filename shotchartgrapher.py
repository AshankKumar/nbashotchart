#for multiple years and slider

from nba_api.stats.static import players
from nba_api.stats.endpoints.shotchartdetail import ShotChartDetail
import pandas as pd
import copy
from plotly.subplots import make_subplots
import plotly.graph_objs as go


string_season = None
seasonList = [] #will be responsible for keep track of the number of subplots throughout the program
court_shapes = []
playerName = None

def getShotData(name, year):
    global string_season
    string_season = f"{str(year)}-{str(year+1)[-2:]}"
    #string_season = 2017-19
    playerID = players.find_players_by_full_name(name)[0]['id']
    shotchart_detail = ShotChartDetail(team_id = 0, player_id = playerID, season_nullable= string_season, context_measure_simple= "FGA")
    shotData = shotchart_detail.get_data_frames()[0]
    shotData["LOC_X"] *= -1
    return shotData

def getShotData2(name, startYear, endYear):
    global string_season
    global seasonList
    global playerName

    playerName = name
    string_season = f"{str(startYear)}-{str(endYear)[-2:]}"
    playerID = players.find_players_by_full_name(name)[0]['id']
    shotDataList = []
    
    for year in range(startYear, endYear): #goes to 2019(endYear-1)
        currentSeason = f"{str(year)}-{str(year+1)[-2:]}"
        seasonList.append(currentSeason)
        shotchart_detail = ShotChartDetail(team_id = 0, player_id = playerID, season_nullable= currentSeason, context_measure_simple= "FGA")
        shotData = shotchart_detail.get_data_frames()[0]
        shotData["LOC_X"] *= -1
        shotDataList.append(shotData)
    return shotDataList

def plotShots2():
    shotDataList = getShotData2("Brook Lopez", 2016, 2019)
    global seasonList

    fig=go.Figure() 
    fig = make_subplots(rows=len(shotDataList), cols=1, subplot_titles=seasonList) #rows set to number of seasons

    shotData = shotDataList[0]
    made_shots = shotData.loc[shotData.SHOT_MADE_FLAG == 1]
    missed_shots = shotData.loc[shotData.SHOT_MADE_FLAG == 0]
    fig.append_trace(go.Scatter(x=made_shots["LOC_X"], y=made_shots["LOC_Y"], mode='markers', marker_color="BLUE", name="Made Shot"), 1,1) 
    fig.append_trace(go.Scatter(x=missed_shots["LOC_X"], y=missed_shots["LOC_Y"], mode='markers', marker_color="Red", name="Missed Shot"), 1,1)
    
    i = 2
    for shotData in shotDataList[1:]: #Can't append all the traces starting from the first set of data in shotDataList since the first subplot must have its legend shown while the rest must not, for stylistic purposes
        made_shots = shotData.loc[shotData.SHOT_MADE_FLAG == 1]
        missed_shots = shotData.loc[shotData.SHOT_MADE_FLAG == 0]
        fig.append_trace(go.Scatter(x=made_shots["LOC_X"], y=made_shots["LOC_Y"], mode='markers', marker_color="BLUE", name="Made Shot", showlegend=False), i,1) 
        fig.append_trace(go.Scatter(x=missed_shots["LOC_X"], y=missed_shots["LOC_Y"], mode='markers', marker_color="Red", name="Missed Shot", showlegend=False), i,1)
        i+=1

    return fig

def makeShapes():
    global court_shapes
    global seasonList

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


    temp_court_shapes = copy.deepcopy(court_shapes)
    i = 2
    for season in seasonList[1:]: #this loop adds more shapes to court_shapes in order for the basketball court to be drawn on all subplots by making new shapes with different xref and yref values
        temp_court_shapes_two = copy.deepcopy(temp_court_shapes)
        for shape in temp_court_shapes_two:
            shape['xref'] = 'x'+ str(i)
            shape['yref'] = 'y' + str(i)
            court_shapes.append(shape)
        i+=1

def drawCourt2():
    global court_shapes
    global seasonList
    global playerName
    global string_season
    fig = plotShots2()
    
    makeShapes()

    layout = go.Layout(
        title= "%s shot data from %s" % (playerName,string_season),
        height=1000,
        width=1000,
        shapes=court_shapes
    )

    for i in range(len(seasonList)): #iterate through each subplot to updates axes
        fig.update_xaxes(dict(showticklabels=False, showgrid=False, zeroline=False),row=i+1,col=1) 
        fig.update_yaxes(dict(showticklabels=False, showgrid=False, zeroline=False),row=i+1,col=1)

    fig.update(layout=layout)
    fig.show()

drawCourt2()
