from flask import Flask, request, render_template, redirect, url_for
import random
import requests
import ipdb
import pickle
import re
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indextest.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
