import tick_data_reader as dr
from m1_ohlc_data import m1_ohlc_data
import definitions as d
from datetime import datetime

import plotly
import plotly.graph_objs as go

if __name__ == '__main__':
    (date, bid, ask) = dr.read_tick_data(d.sample_file, 10000)
    (dates, open_data, high_data, low_data, close_data) = m1_ohlc_data(date, bid)
    trace = go.Candlestick(x=dates,
                            open=open_data,
                            high=high_data,
                            low=low_data,
                            close=close_data)
    data = [trace]
    plotly.offline.plot(data, filename='candlestick_datetime')