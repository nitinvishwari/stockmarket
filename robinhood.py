import robin_stocks as rb 
import pyotp
import sys
import time

lines = open('#####################).read().splitlines()
key = lines[0]
email = lines[1]
passWord = lines[2]
code = lines[3]
totp = pyotp.TOTP(key).now()
login = rb.robinhood.authentication.login(email, passWord, mfa_code=code)

# Getting the price - ticker can be str or list
def Quote(ticker):
	r = rb.robinhood.stocks.get_latest_price(ticker)
	return r

# Buying the stock using limit order
def Buy(ticker, quantity, limit_amount):
	r = rb.robinhood.orders.order_buy_limit(ticker, quantity, limit_amount, 'gtc', True)

# Selling the stock using limit order
def Sell(ticker, quantity, limit_amount):
	r = rb.robinhood.orders.order_sell_limit(ticker, quantity, limit_amount, 'gtc', True)

# Get Symbol using instumentUrl
def getSymbol(instrumentUrl):
	return rb.robinhood.stocks.get_symbol_by_url(instrumentUrl)

# Get Position and quantiy of stocks using ticker
def getPostionAndQuantity(ticker):
	r = rb.robinhood.account.get_open_stock_positions()
	for i in r:
		if(ticker == getSymbol(i['instrument'])):
			return [i['average_buy_price'], i['quantity']]
	return -1

# Cancel All Order in account
def cancelAllOrders():
	r = rb.robinhood.orders.cancel_all_stock_orders()

# Total investment till now
def totalInvestmentAmountTillNow():
	r = rb.robinhood.account.get_open_stock_positions()
	return r




