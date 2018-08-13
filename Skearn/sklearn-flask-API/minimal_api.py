app = Flask(__name__)
@app.route('/api/makecalc/', methods=['POST'])

def makecalc():
	"""
	Function run at each API call.
    No need to re-load the model.
	"""
    # reads the received json 
	jsonfile = request.get_json()
	res = dict()
	for key in jsonfile.keys():
        # calculates and predicts
        res[key] = model.predict(doTheCalculation(key))
	# returns a json file
	return jsonify(res)


if __name__ == '__main__':
    # Model is loaded when the API is launched
	model = pickle.load(open('modelfile', 'rb'))
	app.run(debug=True)
