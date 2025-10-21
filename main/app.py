from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	"""Homepage route returning a small HTML welcome message."""
	return (
		"<html><head><title>Flask App</title></head>"
		"<body><h1>Welcome to the Flask app</h1>"
		"<p>Available endpoints: <code>/health</code>, <code>/data</code></p>"
		"</body></html>",
		200,
		{'Content-Type': 'text/html'}
	)


@app.route('/health', methods=['GET'])
def health():
	"""Simple health check endpoint returning JSON status."""
	return jsonify(status='ok', uptime='unknown'), 200


@app.route('/data', methods=['POST'])
def data():
	"""Accept JSON body and echo it back with a confirmation."""
	if not request.is_json:
		return jsonify(error='Request body must be JSON'), 400

	payload = request.get_json()

	# Basic validation: ensure payload is a dict or list
	if payload is None:
		return jsonify(error='Empty JSON payload'), 400

	return jsonify(received=payload, message='Data received'), 201


if __name__ == '__main__':
	# Run on all interfaces for easy local testing; port 5000 by default
	app.run(host='0.0.0.0', port=5000, debug=True)
