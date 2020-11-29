import pandas as pd
import csv


class FindCommonStocks():
    """
    Identify common stocks between NYSE eodData list, 
    NASDAQ eodData list and yfinance list
    """
    def __init__(self):
        self.yfinancelist = []
        self.NASDAQList = []
        self.NYSEList = []

        self.commonStocksAll = []

    def loadLists(self):
        """
        yfinanceList = special manipulation because we have to find 
        the distinct values (method "value_counts") among the
        huge dataframe
        """
        df_yfinance = pd.read_csv('Historical/marketdata_2017_01_01_DB.csv')['ticker']
        yfDistincs = df_yfinance.value_counts().to_frame().reset_index()
        self.yfinancelist = yfDistincs['index'].to_list()
        self.yfinancelist.sort()
        self.NASDAQList = pd.read_csv('Historical/NASDAQ/NASDAQ_20201118.csv').Symbol.to_list()
        self.NYSEList = pd.read_csv('Historical/NYSE/NYSE_20201120.csv').Symbol.to_list()

    def toSetAndIntersection(self):

        setYfinance = set(self.yfinancelist)
        setNASDAQ = set(self.NASDAQList)
        setNYSE = set(self.NYSEList)

        inter_yf_NASDAQ = list(setYfinance.intersection(setNASDAQ))
        inter_yf_NYSE = list(setYfinance.intersection(setNYSE))

        self.commonStocksAll = inter_yf_NASDAQ + inter_yf_NYSE
        print(self.commonStocksAll)
        print(len(self.commonStocksAll))
        
    def toCSV(self):
        with open('Historical/commonStocksAll.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            for tick in self.commonStocksAll:
                writer.writerows([[tick]])

""" 
        csvwriter = csv.writer(file)
        csvwriter.writerows([[self.commonStocksAll]])
 """
def format():
    newdyfinance = dfyfinance.dropna()
    newdyfinance.to_csv('marketdata_2017_01_01_DB_no_nan.csv', header=False,index=False)


if __name__ == "__main__":
    start = FindCommonStocks()
    start.loadLists()
    start.toSetAndIntersection()
    start.toCSV()



