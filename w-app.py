from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f'(link unavailable)'
        response = requests.get(url)
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return render_template('result.html', location=location, weather_description=weather_description, temperature=temperature, humidity=humidity, wind_speed=wind_speed)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
