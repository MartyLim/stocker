import yfinance as yf

NOT_AVAILABLE = 'N/A'

def get_ticker_info(ticker):
	# ticker = event.input.value.strip().upper()
	# event.input.remove()
	try:
		stock = yf.Ticker(ticker)
		info = stock.info
		stock_info = (
			f"Ticker: {info.get('symbol', NOT_AVAILABLE)}\n"
			f"Name: {info.get('shortName', NOT_AVAILABLE)}\n"
			f"Current Price: {info.get('regularMarketPrice', 'Market Closed')}\n"
			f"Market Cap: {format_number(info.get('marketCap', NOT_AVAILABLE))}\n"
			f"52-Week Range: {info.get('fiftyTwoWeekLow', NOT_AVAILABLE)} - {info.get('fiftyTwoWeekHigh', NOT_AVAILABLE)}"
		)
	except Exception as e:
		stock_info = f"Error fetching data for '{ticker}': {str(e)}"

	return stock_info

def format_number(number: int):
	if number == NOT_AVAILABLE:
		return number 

	if number >= 1000000000000:
		return str((number // 10000000000) / 100) + " t"
	elif number >= 1000000000:		
		return str((number // 10000000) / 100) + " b"
	elif number >= 1000000:
		return str((number // 10000) / 100) + " m"
	else:
		return str(number)