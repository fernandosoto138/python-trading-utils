import tick_data_reader as dr
import definitions as d
from datetime import datetime
from Candlestick import Candlestick


def m1_candlesticks(date, bid):
    candlesticks = []
    current_min = -1
    open_value = 0
    high_value = 0
    low_value = 0
    close_value = 0
    current_date = None
    for i in range(len(date)):
        if(date[i].minute != current_min and current_min != -1):
            candlesticks.append(Candlestick(current_date, open_value,
                                            high_value, low_value,
                                            close_value))
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
    return candlesticks


if __name__ == '__main__':
    (date, bid, ask) = dr.read_tick_data(d.sample_file, 10000)
    m1_cd = m1_candlesticks(date, bid)
    for i in range(len(m1_cd)):
        print(str(i)+" - "+str(m1_cd[i]))
   