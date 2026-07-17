# Crypto Weekly Performance Tracker 🚀

This project is a lightweight data science tool designed to calculate and display the real-time percentage return of popular cryptocurrency pairs (**BTC, ETH, SOL, DOGE, ZEC, XRP**) since the start of the current calendar week (Monday 00:00 UTC).

Unlike platform metrics such as CoinMarketCap's "7d" return which rely on a rolling 168-hour window, this application fixes its anchor point to the **Weekly Open** candle, making it ideal for calendar-based swing trading and institutional weekly trend analysis.

## 📌 Features

*   **Live Market Data:** Fetches real-time prices and weekly open values directly via the public Binance API (No API keys required).
*   **Dynamic Precision Formatting:** Automatically adjusts decimal places based on asset price scale (e.g., handles high-value BTC alongside fractional assets like DOGE seamlessly).
*   **Fault Tolerance:** Built-in error handling ensures the script bypasses temporary API timeouts or connection drops without crashing.
*   **Visual Direction Indicators:** Instantly showcases market momentum using intuitive color/direction emojis.

## 🛠️ Installation

Follow these steps to set up and run the tracker locally:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/crypto-weekly-tracker.git](https://github.com/YOUR_USERNAME/crypto-weekly-tracker.git)
    cd crypto-weekly-tracker
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The project utilizes `requests` and `pandas` for core operations.)*

## 🚀 Usage

Execute the following command in your terminal to fire up the application:

```bash
python app.py


Analysis Time: 2026-07-17 23:15:42
---------------------------------------------------------------------------
Symbol     | Weekly Open ($)      | Current Price ($) | Weekly Return   
---------------------------------------------------------------------------
BTCUSDT    | 62450.50               | 64120.20          | 🔺 +2.67%
ETHUSDT    | 3420.10                | 3385.40           | 🔻 -1.01%
SOLUSDT    | 142.250                | 151.800           | 🔺 +6.71%
DOGEUSDT   | 0.124500               | 0.121200          | 🔻 -2.65%
ZECUSDT    | 28.450                 | 29.100            | 🔺 +2.28%
XRPUSDT    | 0.5840                 | 0.6125            | 🔺 +4.88%



## 📊 Methodology

The application implements the standard financial percentage return formula relative to a fixed start point:

$$\text{Weekly Return} = \frac{\text{Current Price} - \text{Weekly Open Price}}{\text{Weekly Open Price}} \times 100$$

*   **Weekly Open:** The exact opening price of the Binance `1w` candlestick interval (synchronized to Monday 00:00 UTC).
*   **Current Price:** Retrieved asynchronously in real-time from the Binance `/ticker/price` endpoint.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! If you want to expand the project, feel free to check the **Issues** page or open a **Pull Request**. 

Here are some ideas for future roadmap improvements:
1. Adding multi-exchange support (e.g., Coinbase, KuCoin APIs).
2. Implementing automatic local logging (`.csv` or `.json` exports).
3. Developing a simple GUI or web dashboard using Streamlit.
