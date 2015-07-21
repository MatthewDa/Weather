from flask import Flask, render_template, request
import extract


weather_flask=Flask(__name__)

@weather_flask.route('/')
def root():
    return render_template('main.html')

if __name__ == '__main__':
    weather_flask.debug = True
    weather_flask.run(host='0.0.0.0')
