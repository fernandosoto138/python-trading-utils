class Candlestick:
    def __init__(self, datetime, open_val, high_val, low_val, close_val):
        self.datetime = datetime
        self.open = open_val
        self.high = high_val
        self.low = low_val
        self.close = close_val

    def __str__(self):
        return str(self.datetime) + \
            " Open: {0:.5f}".format(self.open) + \
            " High: {0:.5f}".format(self.high) + \
            " Low: {0:.5f}".format(self.low) + \
            " Close: {0:.5f}".format(self.close)
