from flask import Flask, render_template_string
import requests

app = Flask(__name__)

def get_live_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        res = requests.get(url, timeout=3)
        data = res.json()
        return float(data["price"])
    except:
        return "N/A"

@app.route("/")
def index():
    pairs = [
        {"pair": "BTCUSDT", "signal": "🔴 Short", "entry": "105300", "sl": "105550", "tp": "104300", "confidence": "70%"},
        {"pair": "ETHUSDT", "signal": "🟢 Long", "entry": "2520", "sl": "2500", "tp": "2570", "confidence": "80%"},
        {"pair": "SOLUSDT", "signal": "🔴 Short", "entry": "148.80", "sl": "150.00", "tp": "146.00", "confidence": "75%"},
        {"pair": "DOGEUSDT", "signal": "🟢 Long", "entry": "0.1690", "sl": "0.1650", "tp": "0.1750", "confidence": "75%"},
        {"pair": "PEPEUSDT", "signal": "🔴 Short", "entry": "0.00001150", "sl": "0.00001200", "tp": "0.00001060", "confidence": "70%"},
        {"pair": "XRPUSDT", "signal": "🟢 Long", "entry": "0.482", "sl": "0.477", "tp": "0.495", "confidence": "70%"},
        {"pair": "ARBUSDT", "signal": "🟢 Long", "entry": "0.3000", "sl": "0.2900", "tp": "0.3200", "confidence": "80%"},
    ]

    with open("index.html") as f:
        html = f.read()
    rows = ""
    for p in pairs:
        price = get_live_price(p['pair'])
        rows += f"<tr><td>{p['pair']}</td><td>{p['signal']}</td><td>{p['entry']}</td><td>{price}</td><td>{p['sl']}</td><td>{p['tp']}</td><td>{p['confidence']}</td></tr>"
    html = html.replace("<!-- Table rows will be inserted here -->", rows)
    return render_template_string(html)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)