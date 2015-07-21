from flask import Flask, render_template, request
import extract


weather_flask=Flask(__name__)

@weather_flask.route('/')
def root():
    return render_template('main.html')






@weather_flask.route('/weather')
def weather_city():
    return render_template('Azkaban.html')
    # if category == 'Malfoy Manor':

    # if category == 'Shrieking Shack':

    # if category == 'Diagon Alley':

    # if category == 'Hogwarts':

    # if category == 'Azkaban':
   




if __name__ == '__main__':
    weather_flask.debug = True
    weather_flask.run(host='0.0.0.0')










