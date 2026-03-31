# Setup Instructions for Binance Testbot

## Prerequisites
1. **Node.js**: Ensure that Node.js is installed on your machine. You can download it from [nodejs.org](https://nodejs.org/).
2. **Git**: Make sure you have Git installed. You can download it from [git-scm.com](https://git-scm.com/).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/bilalmasood020-hash/testing-bot.git
   cd testing-bot
   ```
2. Install the dependencies:
   ```bash
   npm install
   ```
3. Configure the API keys:
   - Create a `.env` file in the root directory of the project and add your Binance API keys.
   ```plaintext
   BINANCE_API_KEY=your_api_key
   BINANCE_API_SECRET=your_api_secret
   ```

## Strategy Explanations
- **Market Making**: This strategy involves placing buy and sell limit orders to capitalize on the bid-ask spread. The bot will maintain a position close to the market price to take advantage of small price fluctuations.
- **Trend Following**: This strategy involves analyzing market trends and placing trades in the direction of the trend. It uses indicators like Moving Averages to determine entry and exit points.
- **Arbitrage**: This strategy takes advantage of price discrepancies between different exchanges by buying at a lower price on one exchange and selling at a higher price on another.

## Getting Binance Testnet API Keys for Paper Trading
1. Go to the [Binance Testnet](https://testnet.binance.vision/).
2. Click on `Register`, if you do not have an account. Follow the instructions to create a new account.
3. Once registered, log in to your Testnet account.
4. Go to the API Management section and create a new API key.
5. Copy the API key and secret generated, and paste them into your `.env` file as instructed above.

Make sure to use these keys responsibly and only for paper trading on the Testnet.  

## Notes
- Make sure to review the limitations and risks involved in paper trading. This should be used for testing purposes only.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.