import time
from datetime import timedelta
import pandas as pd
class stock(object):
    def __init__(self, stock_type, last_dividend, fixed_dividend, par_value, name):
        self.stock_type = stock_type
        self.last_dividend = last_dividend
        self.fixed_dividend = fixed_dividend
        self.par_value = par_value
        self.name = name  
    TEA = stock("Common", 0, None, 100, "TEA")
    POP = stock("Common", 8, None, 100, "POP")
    ALE = stock("Common", 23, None, 60, "ALE")
    GIN = stock("Preferred", 8, 0.02, 100,"GIN")
    JOE = stock("Common", 13, None, 250, "JOE")  
    def Dividend_Yield(self, market_price):
        if self.stock_type == "Common":
            return(self.last_dividend/market_price)
        else:
            return(self.fixed_dividend*self.par_value/market_price)
    def P_E_Ratio(self, market_price):
        if self.last_dividend==0:
            return("division by zero")
        else:
            return(market_price/self.last_dividend)
    trade_df = pd.DataFrame(columns = ["stock","timestamp","volume", "direction", "price_per_stock"])
    def record(stock,volume, price):
        global trade_df
        timestamp= time.time()
        if volume == 0:
            return("empty volume")
        if volume < 0:
            direction = "Sale"
        else:
            direction = "Buy"
        trade_df = trade_df.append(pd.DataFrame({"stock": stock, "timestamp":timestamp,
                                                 "volume":abs(volume), "direction": direction, 
                                                 "price_per_stock":price},
                                    index=[0]),ignore_index=True) 
import time
from datetime import timedelta

    def volume_weighted_stock_price(datasource):
        datasource = trade_df
        start = time.time() - timedelta(minutes=15).total_seconds()
        trade_15 = trade_df[trade_df["timestamp"]<=start]
        return sum((trade_15["price_per_stock"]*trade_15["volume"]))/sum(trade_15["volume"])
            
    def geo_mean(datasource):
        if datasource.shape[0]==0:
            return("division by zero")
        else:
            return(datasource["price_per_stock"].prod()**(1/datasource.shape[0]))
