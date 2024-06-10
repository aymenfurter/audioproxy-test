from flask import Flask, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    url = "https://crbn.us/whatstheweatherlike.wav"
    response = requests.get(url)
    audio = BytesIO(response.content)
    return send_file(audio, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
