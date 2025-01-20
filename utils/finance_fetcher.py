import yfinance as yf


def get_ticker_info(event):
	ticker = event.input.value.strip().upper()
	event.input.remove()
	try:
		stock = yf.Ticker(ticker)
		info = stock.info
		stock_info = (
			f"Ticker: {info.get('symbol', 'N/A')}\n"
			f"Name: {info.get('shortName', 'N/A')}\n"
			f"Current Price: {info.get('regularMarketPrice', 'Market Closed')}\n"
			f"Market Cap: {format_number(info.get('marketCap', 'N/A'))}\n"
			f"52-Week Range: {info.get('fiftyTwoWeekLow', 'N/A')} - {info.get('fiftyTwoWeekHigh', 'N/A')}"
		)
	except Exception as e:
		stock_info = f"Error fetching data for '{ticker}': {str(e)}"

	return stock_info

def format_number(number: int):
	if number >= 1000000000000:
		return str((number // 10000000000) / 100) + " t"
	elif number >= 1000000000:		
		return str((number // 10000000) / 100) + " b"
	elif number >= 1000000:
		return str((number // 10000) / 100) + " m"
	else:
		return str(number)