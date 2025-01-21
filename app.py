import yfinance as yf
from textual import on
from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Input, Static

from utils.finance_fetcher import get_ticker_info
from utils.config_manager import load_tickers, add_ticker

class StockerApp(App):
	BINDINGS = [
		Binding(key="q", action="quit", description="quit"),
		Binding(key="enter", action="show_input()", description="search ticker", key_display="enter")
	]

	def __init__(self):
		# need to call parent class's __init__
		super().__init__()
		self.tickers = load_tickers()

	def compose(self):
		yield Footer(show_command_palette=False)
		for ticker in self.tickers:
			stock_info = get_ticker_info(ticker)
			yield Static(stock_info)
		# self.stock_output = Static("")
		# yield self.stock_output

	def action_show_input(self):
		input = Input(placeholder="Search by ticker", type="text")
		self.mount(input)
		input.focus()

	@on(Input.Submitted)
	def submit_ticker(self, event):
		ticker = event.value
		self.tickers = add_ticker(ticker)
		event.input.remove()


if __name__ == "__main__":
	app = StockerApp()
	app.run()
