import yaml

TICKERS_KEY = "tickers"

def add_ticker(ticker):
	'''Adds ticker to config and returns new list of Tickers'''
	config = load_config()
	if ticker not in config[TICKERS_KEY]:
		config[TICKERS_KEY].append(ticker)

		with open("config.yaml", "w") as file:
			yaml.dump(config, file)
	
	return config[TICKERS_KEY]

def load_tickers():
	'''Return a list of Tickers from current config'''
	return load_config()[TICKERS_KEY]

def load_config():
	with open("config.yaml", "r") as file:
		config = yaml.safe_load(file)
	
	return config

if __name__ == "__main__":
	load_tickers()
