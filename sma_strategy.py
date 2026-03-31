import pandas as pd
import numpy as np

class SMACrossover:
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window
        self.signal = None

    def generate_signals(self, prices):
        # Calculate short and long moving averages
        signals = pd.DataFrame(index=prices.index)
        signals['price'] = prices
        signals['short_mavg'] = prices.rolling(window=self.short_window, min_periods=1).mean()
        signals['long_mavg'] = prices.rolling(window=self.long_window, min_periods=1).mean()

        # Create signals
        signals['signal'] = 0.0
        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0
        )  

        # Generate buy/sell signals
        signals['positions'] = signals['signal'].diff()
        return signals

    def get_buy_signals(self, signals):
        return signals[signals['positions'] == 1.0]

    def get_sell_signals(self, signals):
        return signals[signals['positions'] == -1.0]

# Example usage:
# prices = pd.Series(...)  # Historical prices
# sma = SMACrossover()
# signals = sma.generate_signals(prices)
# buy_signals = sma.get_buy_signals(signals)
# sell_signals = sma.get_sell_signals(signals)