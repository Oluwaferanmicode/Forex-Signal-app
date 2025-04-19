import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(name)

API_KEY = "baaa367eada24939b18235072c458d5b"  # Replace this with your actual API key CURRENCY_PAIRS = [ "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD", "USD/CAD", "NZD/USD" ]

INDICATORS = ["sma", "ema", "rsi", "macd"] TIMEFRAMES = ["1h", "30min", "15min"]

base_url = "https://api.twelvedata.com"

def fetch_indicator(symbol, interval, indicator): url = f"{base_url}/{indicator}?symbol={symbol}&interval={interval}&apikey={API_KEY}" response = requests.get(url) return response.json()

def analyze_pair(symbol): results = {} for tf in TIMEFRAMES: sma = fetch_indicator(symbol, tf, "sma") ema = fetch_indicator(symbol, tf, "ema") rsi = fetch_indicator(symbol, tf, "rsi") macd = fetch_indicator(symbol, tf, "macd")

try:
        sma_val = float(sma['values'][0]['sma'])
        ema_val = float(ema['values'][0]['ema'])
        rsi_val = float(rsi['values'][0]['rsi'])
        macd_val = float(macd['values'][0]['macd'])
        macd_signal = float(macd['values'][0]['signal'])
    except (KeyError, IndexError, ValueError):
        return {"error": "API error or data missing"}

    signal = "HOLD"
    if sma_val > ema_val and rsi_val > 50 and macd_val > macd_signal:
        signal = "BUY"
    elif sma_val < ema_val and rsi_val < 50 and macd_val < macd_signal:
        signal = "SELL"

    results[tf] = {
        "signal": signal,
        "sma": sma_val,
        "ema": ema_val,
        "rsi": rsi_val,
        "macd": macd_val,
        "macd_signal": macd_signal
    }

return results

@app.route('/') def home(): final_signals = {} for pair in CURRENCY_PAIRS: symbol = pair.replace("/", "") analysis = analyze_pair(symbol) final_signals[pair] = analysis return render_template("index.html", signals=final_signals)

if name == 'main': app.run(debug=True)

