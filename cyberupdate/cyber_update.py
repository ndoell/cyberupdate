'''
Created on Dec 6, 2016

@author: nicholasdoell
'''
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from cyberupdate.CERTFeed import currentactivity

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def cyber_update():
    welcome_msg = render_template('welcome')

    return question(welcome_msg)

@ask.intent("AlertIntent")
def cyber_alerts():
    alerts = 'your in alerts'
    return statement(alerts)


@ask.intent("ActivityIntent")
def cyber_activity():
#    activity = 'your in activity'
    return statement(currentactivity())
#    return question(activity)

if __name__ == '__main__':

    app.run(debug=True)