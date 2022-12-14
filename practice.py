# import pandas
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import linear_model
# from sklearn.metrics import r2_score
# from scipy import stats
#
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# prices = np.array([4297.14, 4305.20, 4274.04, 4283.74, 4228.48, 4137.99, 4128.73, 4140.77, 4199.12, 4057.66, 4030.61, 3986.16,
#                     3955.00, 3966.85, 3924.26, 3908.16, 3979.87, 4006.18, 4067.36, 4110.41])
#
# plt.scatter(x, prices)
# plt.plot(x, prices, '.r-')
#
#     #pandas multiple dependent variables
# df = pandas.read_csv("Sheet1.csv")
# X = df[['Day', 'Change']]
# Y = df['Price']
# regr = linear_model.LinearRegression()
# regr.fit(X, Y)
# # print(regr.coef_)
#
#     # diff is the change in value, changes is 1 if positive, 0 if none or negative
# # diff = prices[1:] - prices[:-1]
# # changes = diff > 0
#
#     # std is standard variation of prices, varience is varience of prices
# std = np.std(prices)
# varience = np.var(prices)
#
#     # linear regression
# slope, intercept, r, p, std_err = stats.linregress(x, prices)
# predict = lambda a: slope * a + intercept
# linModel = list(map(predict, x))
# plt.plot(x, linModel)
# # print(r)
# new = predict(23)
# print(new)
#
#     # polynomial regression
# polyModel = np.poly1d(np.polyfit(x, prices, 4))
# polyLine = np.linspace(1, 20, 4111)
# polyscore = r2_score(prices, polyModel(x))
# plt.plot(polyLine, polyModel(polyLine))
# # print(polyscore)
# new = polyModel(23)
# print(new)
#
#     # logistic regression
# logX = x.reshape(-1,1)
# logr = linear_model.LogisticRegression()
# logr.fit(logX, prices)
# predicted = logr.predict(np.array([23]).reshape(-1, 1))
# print(predicted)
#
# plt.show()
# import time
# import requests
# import csv
#
# with open('tickers.txt', 'r') as f:
#     tickers = f.readlines()
#
# for ticker in tickers:
#     ticker = str(ticker).strip()
#     print(f"getting data for {ticker}")
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey=ZLGDWBU4HK5QHIXT&datatype=csv&outputsize=full"
#
#     try:
#         response = requests.get(url)
#     except Exception as e:
#         print(e)
#         exit(1)
#
#     lines = response.text.splitlines()
#     if 400 < len(lines):
#         lines = lines[:400]
#     reader = csv.reader(lines)
#
#     f = open(f"{ticker}_data.csv", 'w')
#     csv_writer = csv.writer(f)
#     for row in reader:
#         csv_writer.writerow(row)
#
#     f.close()
#
#     time.sleep(15)
#

import Individual
from threading import Lock
b = set()
lstm_pars = {
                'cur_epochs': 20,
                'cur_batch_size': 20,
                'window_size': 50,
                'layer_units': 50
            }

a = Individual.Individual(lstm_pars, b, Lock(), "AAPL")
a.calculate_fitness()
print(b)
