#-*- coding: utf-8 -*-
__author__ = 'aditya'

from foosball import app
from flask import render_template, request, make_response, jsonify, abort, redirect
import requests
import datetime
# from geopy.geocoders import Nominatim
import json

@app.route('/', methods=['GET'])
def home():
    print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    return render_template('index.html')

@app.errorhandler(400)
def page_not_found():
    return render_template("404.html"), 400


# @app.route('/hotel', methods=['GET'])
# def hotel():
#     return render_template('hotel/hotel.html')


# @app.route('/hotel/list', methods=['GET'])
# def hotel_list():
#     return render_template('hotel/hotel_list.html')


@app.route('/hotel/<hotel_id>', methods=['GET'])
def hotel_detail(hotel_id):
    return render_template('hotel/hotel_detail.html')
