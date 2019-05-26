# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State
from plotly import tools
import plotly.graph_objs as go
import pandas as pd
from datetime import date

# Importo Dask

import dask as dask
from dask.distributed import Client, progress
import dask.dataframe as dd

#client = Client()
#client.cluster

# Importo funciones de regresion.py


from regresion import download_info, analisis_p

app = dash.Dash(__name__)

# TOCAYO: función del tocayo para cargar todo
# Aquí debe correr la función que descargue todos los datos.

#lista que especifica lo que se descarga
lista_desc = ["LBMA/GOLD","CHRIS/CME_O1","LBMA/SILVER","CHRIS/CME_DA1","CHRIS/CME_LN1",
              "CHRIS/CME_C1", "CHRIS/CME_RR1", "CHRIS/CME_LB1","CHRIS/CME_RB1", "CHRIS/CME_NG1",
              "CHRIS/CME_PL1","CHRIS/CME_S1"] 

download_info(lista_desc)

# Preferentemente, sería bueno que los guardara en un csv llamado datos.csv =Asi lo hace

nombres_comunes = dict({'LBMA/GOLD': 'Gold',
                        'LBMA/SILVER': 'Silver',
                        'CHRIS/CME_PL1': 'Platinum',
                        'CHRIS/CME_O1': 'Oats',
                        'CHRIS/CME_DA1': 'Dairy',
                        'CHRIS/CME_LN1': 'Pork',
                        'CHRIS/CME_C1': 'Corn',
                        'CHRIS/CME_RR1': 'Rice',
                        'CHRIS/CME_LB1': 'Lumber',
                        'CHRIS/CME_RB1': 'Gasoline',
                        'CHRIS/CME_NG1': 'Natural gas',
                        'CHRIS/CME_S1': 'Soybean'
                        })


colors = {
    'background': '#3d3d3d',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},
                      children=[
    html.H1("Commodities Finance Forecast"),


    html.Div(style={'backgroundColor': colors['background']},
             children=[

                daq.NumericInput(id='LBMA/GOLD',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Gold',
                                 style={'color': '#EFEFEF'}),
                html.Br(),

                daq.NumericInput(id='LBMA/SILVER',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Silver'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_PL1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Platinum'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_O1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Oats'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_DA1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Dairy'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_LN1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Pork'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_C1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Corn'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_RR1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Rice'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_LB1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Lumber'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_RB1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Gasoline'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_NG1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Natural Gas'),
                html.Br(),

                daq.NumericInput(id='CHRIS/CME_S1',
                                 className='numerico',
                                 value=0,
                                 size=100,
                                 min=0,
                                 max=10000,
                                 label='Soybean'),
                html.Br(),

    ], className='listafuturos'),

    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.Label('Investment period',
                           className='commodity'),
                daq.Slider(id='meses',
                           min=2,
                           max=24,
                           marks={'2': '2', '6': '6', '12': '12',
                                  '18': '18', '24': '24'},
                           value=18,
                           size=300,
                           handleLabel='Months'
                           ),
                html.Br(),

                html.Button(html.Span('Estimate returns'),
                            id='botonCalculo',
                            className='boton2'),
                html.Br(),
                html.Br(),
                html.Br(),

    ], className='areacalculo'),

    html.Div(style={'backgroundColor': colors['background']},
             children=[

                html.Img(id='imagenstatus',
                         src=app.get_asset_url('sleep.gif'),
                         className='puerquito'),

                html.P('''Choose the commodities you are interested in,
                       select the investment period and click on the button''',
                       id='textoresultado',
                       className='resultado')

    ], className='areacalculo'),

    dcc.Graph(
        id='grafica_valores',
        figure={
            'data': [
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])


@app.callback([Output('grafica_valores', 'figure'),
               Output('textoresultado', 'children'),
               Output('imagenstatus', 'src')
               ],
              [Input('botonCalculo', 'n_clicks')],
              state=[State('LBMA/GOLD', 'value'),
                     State('LBMA/SILVER', 'value'),
                     State('CHRIS/CME_PL1', 'value'),
                     State('CHRIS/CME_O1', 'value'),
                     State('CHRIS/CME_DA1', 'value'),
                     State('CHRIS/CME_LN1', 'value'),
                     State('CHRIS/CME_C1', 'value'),
                     State('CHRIS/CME_RR1', 'value'),
                     State('CHRIS/CME_LB1', 'value'),
                     State('CHRIS/CME_RB1', 'value'),
                     State('CHRIS/CME_NG1', 'value'),
                     State('CHRIS/CME_S1', 'value'),
                     State('meses', 'value')
                     ]
              )


def update_graph(n_clicks, in1, in2, in3, in4, in5, in6,
                 in7, in8, in9, in10, in11, in12,
                 meses):
    # TOCAYO: Aquí lee el archivo con todos los datos
    df = pd.read_csv('datos.csv') # ya no va a la carpeta de modelo_simple/
    df.Date = pd.to_datetime(df.Date)

    todos = dict({'LBMA/GOLD': in1,
                  'LBMA/SILVER': in2,
                  'CHRIS/CME_PL1': in3,
                  'CHRIS/CME_O1': in4,
                  'CHRIS/CME_DA1': in5,
                  'CHRIS/CME_LN1': in6,
                  'CHRIS/CME_C1': in7,
                  'CHRIS/CME_RR1': in8,
                  'CHRIS/CME_LB1': in9,
                  'CHRIS/CME_RB1': in10,
                  'CHRIS/CME_NG1': in11,
                  'CHRIS/CME_S1': in12
                  })
    validos = dict((k, v) for k, v in todos.items() if v > 0)
    # TOCAYO: Ésta es la lista con todos las commodities con valores
    lista_validos = list(validos.keys())
    
    lista_run = [meses,'0.0001'] #el valor de 0.0001 es la r2 mínima que decidimos
    #dejar baja para reducir el no de bethas, la mantengo por si posteriormente
    # se agrega un scroller con el que se pueda modificar 
    
    lista_run = lista_run+lista_validos
    
    # Corro mi código para calcular rendimientos
    rendim = analisis_p(lista_run)
    cant = list(validos.values())
    rendim['cant']=cant
    
    te = sum(rendim['last_price']*rendim['cant'])
    ga = sum(rendim['predicted_price']*rendim['cant'])
    re = str(round(100*(ga-te)/te,2))+'%'
    
    # Esto no lo entiendo pero lo dejo 
    cols_seleccionar = lista_validos.copy()
    cols_seleccionar.append('Date')
    df = df[df.Date > (date.today() - pd.offsets.MonthBegin(meses))]
    df = df.filter(items=cols_seleccionar)
    df = df.dropna()

    # TOCAYO: Aquí habría que hacer todos los cálculos de las betas y demás
    # texto es la variable que se muestra como output final
    texto = 'The percentual value increase over {} months is {}'.format(meses,
                                                           re)

    
    estatus = app.get_asset_url('work.gif')
    
    lineas = (len(lista_validos) + 1) // 2
    linea = 1
    columna = 1
    fig = tools.make_subplots(rows=lineas, cols=2,
                              subplot_titles=[nombres_comunes[c]
                                              for c in lista_validos])

    for commodity in lista_validos:
        fig.append_trace(go.Scatter(y=df[commodity],
                                    x=df['Date'],
                                    ),
                         linea, columna
                         )
        if columna == 1:
            columna = 2
        elif columna == 2:
            columna = 1
            linea += 1

    fig['layout'].update(yaxis=dict(title='Opening value'),
                         plot_bgcolor=colors['background'],
                         paper_bgcolor=colors['background'],
                         font=dict(color=colors['text']),
                         showlegend=False)

    return fig, texto, estatus




if __name__ == '__main__':
    app.run_server(debug=True)
