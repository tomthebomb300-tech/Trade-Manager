import pandas as pd
import datetime as dt

def loadDf(filename):
    df = pd.read_csv(filename, sep="\t")
    df["Enter Date"] = pd.to_datetime(df["Enter Date"], format="%d-%b-%Y")
    df["Enter Time"] = pd.to_datetime(df["Enter Time"], format="%H:%M").dt.time
    df["Exit Date"] = pd.to_datetime(df["Exit Date"], format="%d-%b-%Y")
    df["Exit Time"] = pd.to_datetime(df["Exit Time"], format="%H:%M").dt.time
    return df

def getProfitLoss(df):
    return round(df['P&L'].sum(),2)

def getWinRate(df):
    wins = df[df["Outcome"] == "Win"]
    winRate = round(len(wins)/len(df)*100,2)
    return winRate

def getAvgProfit(df):
    wins = df[df['P&L'] > 0]
    average = round(wins['P&L'].sum()/len(wins),2)
    return average

def getAvgLoss(df):
    losses = df[df['P&L'] < 0]
    average = round(losses['P&L'].sum()/len(losses),2)
    return average

def getProfitFactor(df):
    totalProfits = round(df[df['P&L'] > 0]['P&L'].sum(),2)
    totalLosses = round(df[df['P&L'] < 0]['P&L'].sum(),2)*-1
    return round(totalProfits/totalLosses,2)

def startup():
    return loadDf("stockDayTrades.csv")