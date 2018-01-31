import tick_data_reader as dr
import definitions as d
from datetime import datetime


def m1_ohlc_data(date, bid):
    dates = []
    open_data = []
    high_data = []
    low_data = []
    close_data = []
    current_min = -1
    open_value = 0
    high_value = 0
    low_value = 0
    close_value = 0
    current_date = None
    for i in range(len(date)):
        if(date[i].minute != current_min and current_min != -1):
            dates.append(current_date)
            open_data.append(open_value)
            high_data.append(high_value)
            low_data.append(low_value)
            close_data.append(close_value)
        if(date[i].minute != current_min):
            current_min = date[i].minute
            current_date = date[i]
            open_value = bid[i]
            low_value = bid[i]
            high_value = bid[i]
        if(bid[i] > high_value):
            high_value = bid[i]
        if(bid[i] < low_value):
            low_value = bid[i]
        close_value = bid[i]
    return (dates, open_data, high_data, low_data, close_data)
