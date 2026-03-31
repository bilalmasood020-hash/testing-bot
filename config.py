# Trading Bot Configuration

exchange = {
    'name': 'Binance',
    'api_key': 'YOUR_API_KEY',
    'api_secret': 'YOUR_API_SECRET',
    'testnet': True,
}

strategy = {
    'name': 'Simple Moving Average',
    'short_window': 10,
    'long_window': 50,
}

risk_management = {
    'risk_percentage': 2,
    'take_profit': 1.5,
    'stop_loss': 1.0,
}

paper_trading = {
    'enabled': True,
    'symbol': 'BTC/USDT',
    'initial_balance': 10000,
}