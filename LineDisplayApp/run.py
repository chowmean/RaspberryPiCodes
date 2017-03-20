#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from subprocess import call
import json
import datetime
import subprocess
import requests
call(["ls", "-l"])

app = Flask(__name__)

@app.route('/uber')
def index():
	a = subprocess.check_output(["uber","time","'opera brindawan appartments'"])
	location = a.split('│')[1]
	location = location.strip(" ")
	time = a.split('│')[6]
	time = time.strip(" ")
	car = a.split('│')[7]
	car = car.strip(" ")
	return jsonify({'location': location, 'car': car, 'time': time})

@app.route('/time')
def time():
	return jsonify({"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

@app.route('/weather')
def weather():
	a = requests.get("http://samples.openweathermap.org/data/2.5/weather?id=1277333&appid=b1b15e88fa797225412429c1c50c122a1")
	return jsonify({'weather':json.loads(a.content)["main"]})
if __name__ == '__main__':
    app.run(debug=True)