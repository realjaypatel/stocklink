from fastapi import FastAPI, Request
from router import stock


app = FastAPI()


app.include_router(stock.router)