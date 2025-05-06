from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I'm Flask"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway will inject PORT, fallback to 5000 locally
    app.run(host='0.0.0.0', port=port)
