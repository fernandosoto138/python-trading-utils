import urllib.request
from multiprocessing import Process

# Available Currencies 
# AUDCAD,AUDCHF,AUDJPY, AUDNZD,CADCHF,EURAUD,EURCHF,EURGBP
# EURJPY,EURUSD,GBPCHF,GBPJPY,GBPNZD,GBPUSD,GBPCHF,GBPJPY
# GBPNZD,NZDCAD,NZDCHF.NZDJPY,NZDUSD,USDCAD,USDCHF,USDJPY

def DownloadTickData(symbol, year, week_count):
    base = 'https://tickdata.fxcorporate.com/'+symbol+'/'+str(year)+'/'
    extension = '.csv.gz'
    for week in range(1, week_count+1):
        url = base + str(week) + extension
        print("Downloading week: "+str(week))
        print("\t" + url)
        f = open(str(year)+"_"+symbol+"_WEEK_"+str(week)+extension, "wb")
        response = urllib.request.urlopen(url)
        data = response.read()      
        f.write(data)
        f.close()

currency = 'USDJPY'
if __name__ == '__main__':
    p1 = Process(target=DownloadTickData, args=(currency, 2015, 53,))
    p2 = Process(target=DownloadTickData, args=(currency, 2016, 52,))
    p3 = Process(target=DownloadTickData, args=(currency, 2017, 52,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()