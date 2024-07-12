
import yfinance as yahooFinance
 
# Here We are getting Facebook financial information
# We need to pass FB as argument for that
x = 0
while True:
    GetFacebookInformation = yahooFinance.Ticker("TATASTEEL.NS")
    print(GetFacebookInformation.info,x)
    x+=1