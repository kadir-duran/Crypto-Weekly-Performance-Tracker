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
    git clone [https://github.com/kadir-duran/crypto-weekly-tracker.git](https://github.com/kadir-duran/crypto-weekly-tracker.git)
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
```
