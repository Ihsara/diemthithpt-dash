# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
from pathlib import Path



__file__ = "../dat/province_code.xlsx"
BASE_DIR_DATA = "../dat/{}.csv"


def get_data(ref_province):
    data_wrapper = {}
    for province_id in range(64):
        try:
            data_wrapper[ref_province[ref_province["SỐ TT CỤM THI"] == province_id]["ĐIẠ PHƯƠNG"].values[0]] = pd.read_csv(BASE_DIR_DATA.format(province_id))
        except FileNotFoundError:
            pass
    return data_wrapper

province_ref = pd.read_excel(__file__)
data_wrapper = get_data(province_ref)


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.P(children='''
        This is the test paragraph
    '''),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                        go.Histogram(x=data_wrapper["TP.HCM"]['LÝ'],  histnorm='probability')
            ],
            'layout': {
                'title': 'Điểm thi Toán THPT của TP.HCM 2018'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)