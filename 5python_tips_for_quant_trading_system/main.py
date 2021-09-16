import datetime as dt
from datetime import timedelta
import pandas as pd
import pytz
import math


def get_prev_tstamp(itvl, curr_dt):
    if itvl[-1] == 'm':
        prev_dt = curr_dt - timedelta(minutes=int(itvl[:-1]))
    elif itvl[-1] == 'h':
        prev_dt = curr_dt - timedelta(hours=int(itvl[:-1]))
    elif itvl[-1] == "d":
        prev_dt = curr_dt - timedelta(days=int(itvl[:-1]))
    return prev_dt


def get_next_tstamp(itvl, curr_dt):
    if itvl[-1] == 'm':
        next_dt = curr_dt + timedelta(minutes=int(itvl[:-1]))
    elif itvl[-1] == 'h':
        next_dt = curr_dt + timedelta(hours=int(itvl[:-1]))
    elif itvl[-1] == "d":
        next_dt = curr_dt + timedelta(days=int(itvl[:-1]))
    return next_dt


itvl = '6d'
curr_dt = dt.datetime(2021, 9, 15, 17, 27)
curr_dt
prev_dt = get_prev_tstamp(itvl, curr_dt)
prev_dt
next_dt = get_next_tstamp(itvl, curr_dt)
next_dt

df1 = pd.DataFrame({"Close": [100, 110, 120]}, index=["Day1", "Day2", "Day3"])
df2 = pd.DataFrame({"Close": [130, 140, 150]}, index=["Day4", "Day5", "Day6"])


def concat_rows(df1, df2):
    df3 = pd.concat([df1, df2])
    return df3


df3 = concat_rows(df1, df2)
df3

df4 = pd.DataFrame({"MA": df1['Close'].rolling(2).mean()}, index=["Day1", "Day2", "Day3"])


def concat_cols(df1, df2):
    df3 = pd.concat([df1, df2], axis=1)
    return df3


df5 = concat_cols(df1, df4)
df5

curr_dt = dt.datetime(2021, 9, 15, 13, 25, 4)



def get_date_range():
    holidays = []
    curr_dt = dt.datetime(2021, 9, 15, 13, 0, 0)
    sim_idx = pd.date_range(start=curr_dt, freq='1h', periods=100)
    df = pd.DataFrame(index=sim_idx)
    df['Weekday'] = df.index.day_name()
    df['Date'] = df.index.date
    df['Time'] = df.index.time

    df = df[~df["Weekday"].isin(['Saturday', "Sunday"])]
    df = df[~df['Date'].isin([holidays])]
    df = df[df['Time'] >= dt.time(hour=11, minute=0)]
    df = df[df['Time'] <= dt.time(hour=16, minute=0)]
    tstamp_range = df.index.copy()
    return tstamp_range
