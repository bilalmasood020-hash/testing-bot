import time

class TradingBot:
    def __init__(self):
        self.strategies = []  # Initialize strategies here

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def run(self):
        while True:
            for strategy in self.strategies:
                strategy.execute()  # Execute strategy
            time.sleep(1)  # Delay for a second (adjust as necessary)

if __name__ == '__main__':
    bot = TradingBot()
    # Add strategies to the bot
    # bot.add_strategy(SomeStrategy())
    bot.run()