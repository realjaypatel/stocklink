from fastapi import APIRouter
import yfinance as yahooFinance

router = APIRouter()

async def fetch_data(ticker):
    stockdata = yahooFinance.Ticker(ticker)
    stockdata = stockdata.info


@router.get("/ticker/{ticker}")
async def read_root(ticker):
    stockdata = fetch_data(ticker)

    return {"data": stockdata}