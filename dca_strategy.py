def dollar_cost_averaging(investment_amount, frequency, total_periods):
    """
    Implements the Dollar Cost Averaging (DCA) strategy.

    Parameters:
    - investment_amount: Amount to invest at each interval
    - frequency: How often to invest (e.g., monthly, weekly)
    - total_periods: Total number of investments to make

    Returns:
    - A list of investments made
    """
    investments = []
    for period in range(total_periods):
        investments.append(investment_amount)
        print(f"Invested {investment_amount} at period {period + 1}")
    return investments

# Example of using the DCA strategy
if __name__ == '__main__':
    investment_per_period = 100  # For example, $100
    investment_frequency = 'monthly'  # Monthly investments
    investment_duration = 12  # For a year
    dollar_cost_averaging(investment_per_period, investment_frequency, investment_duration)