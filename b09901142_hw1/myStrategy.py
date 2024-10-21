import sys
import numpy as np
import pandas as pd
import talib
def myStrategy(pastPriceVec, currentPrice, alpha=25, beta=75, rsi_period=14, bollinger_period=8):
    action=0
    alpha = 22
    beta = 83
    rsi_period = 16
    bollinger_period = 16
    dataLen = len(pastPriceVec)
    if dataLen == 0:
        return action
        
    # Compute RSI
    rsi = talib.RSI(pastPriceVec, timeperiod=rsi_period)
    
    # Compute Bollinger Bands
    upper, middle, lower = talib.BBANDS(pastPriceVec, timeperiod=bollinger_period, nbdevup=2, nbdevdn=2, matype=0)
    
    
    # Determine action
    # Buy if MACD Histogram is positive, RSI is below 30 (oversold) and price is below the lower Bollinger Band
    if rsi[-1] < alpha and currentPrice < lower[-1]:
        action = 1
    # Sell if MACD Histogram is negative, RSI is above 70 (overbought) and price is above the upper Bollinger Band
    elif rsi[-1] > beta and currentPrice > upper[-1]:
        action = -1
    else:
        action = 0
    
    return action