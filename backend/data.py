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

def getDailyPL(df):
    dates = df['Exit Date'].unique()
    dates = sorted(dates)

    dailyInfo = []
    balance = 0
    for date in dates:
        balance += df[df['Exit Date'] == date]['P&L'].sum()
        dailyInfo.append(
            {
                'date' : date,
                'balance' : round(balance,2)
            }
        )
    return dailyInfo

def getWeeklyDetails(df):
    weekStart = dt.datetime(2026,1,1)
    weekEnd = dt.datetime(2026,1,9)
    currentDate = dt.datetime.today()
    weeklyInfo = []
    weekCounter = 1
    runningProfit = 0
    while(weekStart < currentDate):
        trades = df[(df['Exit Date'] >= weekStart) & (df['Exit Date'] <= weekEnd)]
        profit = trades['P&L'].sum()
        runningProfit += profit
        weekName = "Week "+str(weekCounter)
        weeklyInfo.append(
            {
                'Name' : weekName,
                'Profit' : round(profit,2),
                'Running Profit' : round(runningProfit,2),
                'Number Wins' : len(trades[trades['Outcome'] == 'Win']),
                'Number Losses' : len(trades[trades['Outcome'] == 'Loss']),
                'Start Date' : str(weekStart.date()),
                'End Date' : str(weekEnd.date())
            }
        )
        weekStart = weekEnd + dt.timedelta(days=3)
        weekEnd = weekStart + dt.timedelta(days=4)
        weekCounter += 1
    return weeklyInfo
        

def startup():
    return loadDf("stockDayTrades.csv")