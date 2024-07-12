from fastapi import FastAPI, Request

app = FastAPI()


import yfinance as yahooFinance



@app.get("/ticker/{ticker}")
async def read_root(ticker):
    stockdata = yahooFinance.Ticker(ticker)
    stockdata = stockdata.info
    return {"data": stockdata}