from tvDatafeed import TvDatafeed, Interval

username = 'pjay32547@gmail.com'
password = 'softlinkJ@3'

tv = TvDatafeed(username, password)
nifty_index_data = tv.get_hist(symbol='NIFTY',exchange='NSE',interval=Interval.in_1_hour,n_bars=10000)
print(nifty_index_data)
