def read_tick_data(file_location, samples_count=-1):
    with open(file_location, 'r') as file:
        count = 0
        date = []
        bid = []
        ask = []
        # skip first line
        file.readline()
        for line in file:
            if(len(line) > 5):
                # for some reason the data have a lot of null characters \x00
                # we need to remove it
                line = line.replace("\x00", "")
                data = line.split(",")
                date.append(data[0])
                bid.append(float(data[1]))
                ask.append(float(data[2]))
                count += 1
                if count > samples_count and samples_count >= 0:
                    break
        return (date, bid, ask)

if __name__ == '__main__':
    sample_file = '/Volumes/Data/ForexTickData/EURUSD/2015_EURUSD_WEEK_1.csv'
    samples_count = 10
    (date, bid, ask) = read_tick_data(sample_file, samples_count)
    for i in range(len(date)):
        print(str(date[i])+" Bid: "+str(bid[i])+" Ask: "+str(ask[i]))
