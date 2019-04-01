#-*- coding: utf-8 -*-
__author__ = 'aditya'

from foosball import app
from flask import render_template, request, make_response, jsonify, abort, redirect
import requests
import datetime
# from geopy.geocoders import Nominatim
import json

print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee1111111111111111111")
@app.route('/', methods=['GET'])
def home():
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    return render_template('index.html')

@app.errorhandler(400)
def page_not_found():
    return render_template("404.html"), 400



