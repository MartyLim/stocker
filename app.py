import yfinance as yf
from textual import on
from textual.app import App
from textual.binding import Binding
from textual.widgets import Footer, Input, Static

from utils.finance_fetcher import get_ticker_info

class StockerApp(App):
	BINDINGS = [
		Binding(key="q", action="quit", description="quit"),
		Binding(key="enter", action="show_input()", description="search ticker", key_display="enter")
	]

	def compose(self):
		yield Footer(show_command_palette=False)
		self.stock_output = Static("")
		yield self.stock_output

	def action_show_input(self):
		input = Input(placeholder="Search by ticker", type="text")
		self.mount(input)
		input.focus()

	@on(Input.Submitted)
	def submit_ticker(self, event):
		stock_info = get_ticker_info(event)
		self.stock_output.update(stock_info)


if __name__ == "__main__":
	app = StockerApp()
	app.run()
