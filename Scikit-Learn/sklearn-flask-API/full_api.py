import numpy as np
import pandas as pd
from datetime import date

from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import pickle

def doTheCalculation(data):
	data['dayofyear']=(data['dteday']- 
    data['dteday'].apply(lambda x: date(x.year,1,1))
    .astype('datetime64[ns]')).apply(lambda x: x.days)

	X = np.array(data[['instant','season','yr','holiday','weekday','workingday',
    'weathersit','temp','atemp','hum','windspeed','dayofyear']])
	return X


app = Flask(__name__)
@app.route('/api/makecalc/', methods=['POST'])
def makecalc():
	"""
	Function run at each API call
	"""
	jsonfile = request.get_json()
	data = pd.read_json(json.dumps(jsonfile), orient='index', convert_dates=['dteday'])

	print(data)
	res = dict()
	ypred = model.predict(doTheCalculation(data))
	for i in range(len(ypred)):
    		res[i] = ypred[i]
	return jsonify(res)

if __name__ == '__main__':
    modelfile = 'modelfile.pickle'
    model = pickle.load(open(modelfile, 'rb'))
    print("loaded OK")
    app.run(debug=True)