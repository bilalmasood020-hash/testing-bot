def mean_reversion_strategy(prices):
    """
    Implements a simple mean reversion strategy.
    Buys when the price is below the moving average and sells when it is above.
    """
    import numpy as np

    # Calculate the moving average
    moving_average = np.mean(prices)
    last_price = prices[-1]

    if last_price < moving_average:
        return "Buy"
    elif last_price > moving_average:
        return "Sell"
    else:
        return "Hold"


# Example usage:
if __name__ == '__main__':
    price_data = [100, 102, 101, 98, 95, 99, 105, 107]
    action = mean_reversion_strategy(price_data)
    print(f"Action to take: {action}")