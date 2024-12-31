from flask import Flask
import requests

#url =   'https://b89c-102-89-40-34.ngrok-free.app/'
#headers = {"ngrok-skip-browser-warning": "1"}

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Muhammad Muhammad Yusuf"

if __name__ == '__main__':
    app.run(debug=True)